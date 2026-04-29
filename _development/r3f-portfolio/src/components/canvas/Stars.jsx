import { useState, useRef, Suspense } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { Points, PointMaterial, Preload } from "@react-three/drei";
import * as random from "maath/random/dist/maath-random.esm";

const Stars = (props) => {
  const ref = useRef();

  /* 
  const [positions] = random.inSphere(new Float32Array(600), { radius: 1.2 });
  for (let i = 0; i < positions.length; i++) {
    if (isNaN(positions[i])) {
      console.error(`NaN value found at index ${i}`);
      positions[i] = 0; // Replace NaN with a default value
    }
  }
 */

  const [starsPosition] = useState(() =>
    random.inSphere(new Float32Array(5001), { radius: 1.2 })
  );

  useFrame((state, delta) => {
    ref.current.rotation.x -= delta / 10;
    ref.current.rotation.y -= delta / 15;
  });

  return (
    <group rotation={[0, 0, Math.PI / 4]}>
      <Points
        ref={ref}
        positions={starsPosition}
        stride={3}
        frustumCulled
        {...props}
      >
        <PointMaterial
          transparent
          color="#f272c8"
          size={0.002}
          sizeAttenuation={true}
          depthWrite={false}
        />
      </Points>
    </group>
  );
};

const StarsCanvas = () => {
  return (
    <div className="w-full h-auto absolute inset-0 z-[-1]">
      <Suspense fallback={null}>
        <Canvas
          gl={{ preserveDrawingBuffer: true }}
          camera={{ position: [0, 0, 1] }}
        >
          <Stars />
          <Preload all />
        </Canvas>
      </Suspense>
    </div>
  );
};

export default StarsCanvas;
