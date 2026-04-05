import React, { Suspense } from "react";

import { Canvas } from "@react-three/fiber";
import { OrbitControls, Preload, useGLTF } from "@react-three/drei";
/*
  1. for render broked 
    - use `npm install --legacy-peer-deps three`
  2. encounting massive `Unknown property ... eslint` error
    - use `npm install @react-three/eslint-plugin --save-dev`  
*/

// import UseDviceSize from "../usehooks/UseDviceSize";
// only for debug as single component

import CanvasLoader from "../Loader";
import { isMobileSafari } from "react-device-detect";

// isMobile as State check if mobile for adjust
const DesktopPC = ({ isMobile, isTablet }) => {
  const desktopModel = useGLTF("./desktop_pc/scene.gltf");
  /* 
    more gltf models can be found
    https://free3d.com/3d-models/
    https://sketchfab.com/features/free-3d-models
  */

  // const { isMobile, isTablet } = UseDviceSize();
  // useState function param for debug when single component.

  return (
    <mesh>
      <hemisphereLight
        /* some origin variable not correctly function, 
        check the variable if the lights not casting right position */
        intensity={0.25} /* origin = 0.15 */
        groundColor="black"
      />

      <spotLight
        position={[0, 5.25, -1.25]}
        /* for adjust */
        angle={Math.PI / 4} /* origin = 0.12 */
        // if on some other device does not correctly having light enable following intensity
        // intensity={300} /* debug */
        penumbra={1.0}
        castShadow
        shadow-mapSize={1024}
      />

      <pointLight
        intensity={1.75} /* origin = 1 */
        position={
          isMobile && isMobileSafari
            ? [0, -0.55, 0]
            : isMobile
            ? [0, -0.9, 0]
            : isTablet
            ? [0, -0.65, -0.25]
            : [0, -0.55, -0.25]
        } /* adding for adjust both mobile or web */
        color={"#ffffff"} /* prevent lights opacity */
        castShadow
      />

      <primitive
        object={desktopModel.scene}
        // add mobile adjust state listener
        // control desktopPC_Canvas total scale
        scale={
          isMobile && isMobileSafari
            ? 0.425
            : isMobile
            ? 0.475
            : isTablet
            ? 0.7
            : 0.825
        } /* mobile origin = 0.7 */
        position={
          // control position on screen in [x,y,z]
          isMobile && isMobileSafari
            ? [0, -2.05, -0.55]
            : isMobile
            ? [0, -2.45, -0.705]
            : isTablet
            ? [-0.14, -3.55, -1.25]
            : [0, -4.05, -1.25]
        }
        /*
          extra y[corr] adjust for text typewrittver
          mobile origin = [0, -3, -2.2]
          web origin = [0, -3.25, -1.5]
        */
        rotation={
          isMobile || isMobileSafari
            ? [-0.01, 0.26, -0.16]
            : [-0.01, -0.42, -0.12]
        } // origin = [-0.01, -0.2, -0.1]
      />
    </mesh>
  );
};

const DesktopCanvas = ({ isMobile, isTablet }) => {
  // UseDviceSize params

  return (
    <Canvas
      frameloop="demand"
      shadows
      // SoftShadows // some browser not work
      camera={{ position: [20, 3, 5], fov: 25 }}
      gl={{ preserveDrawingBuffer: true }}
      eventPrefix="offset"

      // style={{ pointerEvents: "none" }}
      // Attach event listeners conditionally based on device type
    >
      <Suspense
        /* lodaer prevent app breakdown cause by browser delay */ fallback={
          <CanvasLoader />
        }
      >
        <OrbitControls
          enableZoom={false}
          maxPolarAngle={Math.PI / 2}
          minPolarAngle={Math.PI / 2}
        />
        {/* Pass the isMobile and isTablet props to DesktopPC */}
        <DesktopPC isMobile={isMobile} isTablet={isTablet} />
      </Suspense>

      <Preload all />
    </Canvas>
  );
};

export default DesktopCanvas; // Make sure to export DesktopCanvas
