import React, { useEffect, useRef } from "react";
import Tilt from "react-parallax-tilt";
import { motion } from "framer-motion";
import { DotLottieReact } from "@lottiefiles/dotlottie-react";

// Stages for the fade-in effect
const showVariants = {
  show: { opacity: 1, y: 0, transition: { duration: 0.5 } },
  hidden: { opacity: 0, y: 50, transition: { duration: 0.8 } },
};

// Variants for the 3D "pop-out" effect
const popOutVariants = {
  rest: {
    z: 0,
    scale: 1,
    transition: { duration: 0.6 },
  },
  popOut: {
    z: 80,
    scale: 1.15,
    transition: { duration: 0.4 },
  },
};

//

const AboutServiceTilt = ({ icon, title, content }) => {
  const lottieRef = useRef(null);

  useEffect(() => {
    if (lottieRef.current) {
      console.log("Renderer:", lottieRef.current.getRendererType()); // Debug renderer
    }
  }, []);

  return (
    <motion.div // Animate the card appearance
      variants={showVariants}
      className="w-[90%] md:w-[360px] lg:w-[440px] rounded-[20px] shadow-card bg-opacity-50 p-[8px] mx-auto my-4 lg:my-10"
    >
      <Tilt // Parallax tilt effect
        perspective={700}
        glareEnable={true}
        glareMaxOpacity={0.45}
        glareBorderRadius="18px"
        scale={1.02}
        gyroscope={false}
        className={`flex flex-wrap h-[360px] rounded-2xl shadow-lg preserve-3d bg-tertiary border-2 bd-dialog-gradient`}
      >
        <motion.div // Apply the pop-out effect
          initial="rest"
          animate="rest"
          whileHover="popOut"
          variants={popOutVariants}
          className="w-full h-full flex flex-col justify-evenly items-center py-5"
        >
          <DotLottieReact // Lottie animation component
            /* lottieRef={lottieRef} */
            renderer="svg"
            renderConfig={"svg"} // Trying use Svg for svg rendering
            src={icon}
            alt={title}
            autoplay
            loop // Enable if needed
            speed={0.9} // Lower speed for less CPU usage
            className="w-32 h-32 object-contain"
          />
          <h3 className="text-white text-[2rem] font-bold text-center">
            {title}
          </h3>
          <p className="text-white text-center">{content}</p>
        </motion.div>
      </Tilt>
    </motion.div>
  );
};

export default AboutServiceTilt;

// Previous version of the Hover parallax effect
// Inline styles
/* const parallaxEffect = {
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  alignItems: "center",
  width: "220px",
  height: "160px",
  // backgroundColor: "darkgreen",
  // color: "white",
  border: "5px solid black",
  borderRadius: "20px",
  transformStyle: "preserve-3d",
  background:
    // "repeating-linear-gradient(45deg, #015f01, #015f01 30px, #077407 30px, #077407 60px)",
    "linear-gradient(90deg, rgba(131,58,180,0.9) 0%, rgba(253,160,29,0.9) 50%, rgba(252,69,69,0.6) 100%)",
}; */
