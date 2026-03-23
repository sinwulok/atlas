import React, { Suspense, useRef } from "react";
import { useFrame, Canvas } from "@react-three/fiber";
import { OrbitControls, Preload, useGLTF } from "@react-three/drei";
import CanvasLoader from "../Loader";

const VendingMachineModel = ({ isMobile, isTablet }) => {
  const vendingModel = useGLTF("/vending_machine/scene.gltf");
  const meshRef = useRef();

  useFrame((state) => {
    const t = state.clock.getElapsedTime();
    if (meshRef.current) {
      // 泡泡飄動：上下+左右+旋轉
      meshRef.current.position.y = Math.sin(t) * 2 + (isMobile ? -5.99 : -3);
      meshRef.current.position.x = Math.cos(t * 0.7) * 2 + (isMobile ? 0 : isTablet ? 1 : 2);
      meshRef.current.rotation.y = Math.sin(t * 0.5) * 0.5 + (isMobile ? -Math.PI / 2 : -2.5);
      meshRef.current.rotation.x = Math.cos(t * 0.3) * 0.1 + (isMobile ? 0 : isTablet ? -0.4 : 0.2);
    }
  });

  return (
    <mesh>
      <hemisphereLight intensity={1} groundColor="black" />
      <spotLight position={[0, 5, 0]} angle={Math.PI / 4} penumbra={1.0} castShadow shadow-mapSize={1024} />
      <pointLight intensity={0.2} position={[0, 2, 2]} color={"#ffffff"} castShadow />
      <primitive
        ref={meshRef}
        object={vendingModel.scene}
        scale={isMobile ? 90 : isTablet ? 60 : 70}
      />
    </mesh>
  );
};

const VendingCanvas = ({ isMobile, isTablet }) => {
  return (
    <Canvas
      frameloop="demand"
      shadows
      camera={{ position: [0, 2, 8], fov: 25 }}
      gl={{ preserveDrawingBuffer: true }}
      eventPrefix="offset"
      style={{ width: "100%", height: "100%" }}
    >
      <Suspense fallback={<CanvasLoader />}>
        <OrbitControls enableZoom={true} maxPolarAngle={Math.PI / 2} minPolarAngle={0} />
        <VendingMachineModel isMobile={isMobile} isTablet={isTablet} />
      </Suspense>
      <Preload all />
    </Canvas>
  );
};

export default VendingCanvas;
