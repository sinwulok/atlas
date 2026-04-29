import React, { useState } from "react";

import Tilt from "react-parallax-tilt";

import { motion } from "framer-motion";

// import "./ParallaxEffectGlareScale.demozap.css";

const showVariants = {
  show: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.5,
    },
  },
  hidden: {
    opacity: 0,
    y: 50,
    transition: {
      duration: 0.5,
    },
  },
};

// Variants for the 3D "pop-out" effect
const popOutVariants = {
  rest: {
    z: 20,
    transition: {
      duration: 0.5,
    },
  },
  popOut: {
    z: 60,
    transition: {
      duration: 0.5,
    },
  },
};

// Inline styles
const parallaxEffect = {
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  alignItems: "center",
  // width: "300px",
  // height: "300px",
  backgroundColor: "darkgreen",
  color: "white",
  border: "5px solid black",
  borderRadius: "20px",
  transformStyle: "preserve-3d",
  background:
    "repeating-linear-gradient(45deg, #015f01, #015f01 30px, #077407 30px, #077407 60px)",
};

const AboutServiceTilt = () => {
  const [isHovered, setIsHovered] = useState(false);
  return (
    <motion.div variants={showVariants}>
      <Tilt
        // className="parallax-effect"
        perspective={500}
        glareEnable={true}
        glareMaxOpacity={0.45}
        scale={1.02}
        gyroscope={true}
        style={parallaxEffect}
      >
        <motion.div
          initial="rest"
          animate={isHovered ? "popOut" : "rest"}
          variants={popOutVariants}
          className=" h-auto items-center "
        >
          <div className="text-xl">React</div>
          <div>Parallax Tilt</div>
          <div>👀</div>
        </motion.div>
      </Tilt>
    </motion.div>
  );
};

export default AboutServiceTilt;
