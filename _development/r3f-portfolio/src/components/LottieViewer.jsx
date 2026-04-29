import React, { useState, useEffect } from "react";
import { DotLottieReact } from "@lottiefiles/dotlottie-react";
import animationStatic from "../assets/lotties/fullstack.lottie"; // Keep static import

const LottieViewer = () => {
  const [animation, setAnimation] = useState(null);

  useEffect(() => {
    // Try lazy loading the .lottie file
    import("../assets/lotties/fullstack.lottie")
      .then((mod) => {
        setAnimation(mod.default);
      })
      .catch(() => {
        // Fallback to static import if dynamic import fails
        setAnimation(animationStatic);
      });
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold text-center mb-8">Lottie Viewer</h1>

      {/* 測試 animation1 */}
      <div className="flex flex-col items-center justify-center border rounded-lg p-4 shadow-lg">
        {animation ? (
          <DotLottieReact
            autoplay
            loop
            src={animation}
            style={{ height: "300px", width: "300px" }}
          />
        ) : (
          <div className="h-[300px] w-[300px] flex items-center justify-center">
            Loading...
          </div>
        )}
        <h2 className="text-lg font-semibold mt-4">Animation 1</h2>
      </div>
    </div>
  );
};

export default LottieViewer;
