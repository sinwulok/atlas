import React from "react";
import Tilt from "react-parallax-tilt";

import { motion, px, transform } from "framer-motion";
import "../utils/parallax.css";

/* tilt responsive 3d cards */
const AboutServiceTilt = ({ index, title, icon }) => {
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
  const parallaxVariants = {
    rest: {
      transform: "translateZ(0px)",
      transition: {
        duration: 0.5,
        type: "tween",
      },
    },
    hover: {
      transform: "translateZ(100px)",
      duration: 0.5,
      type: "tween",
    },
  };

  const parallaxAnimate = {
    initial: {
      transform: "translateZ(0px)",
    },
    animate: {
      transform: "translateZ(100px)",
      transition: {
        type: "spring",
        stiffness: 20,
        restDelta: 2,
      },
    },
  };

  return (
    <Tilt
      className="xs:w-[250px] w-full"
      /* 
        original options settings in `card content` element
        option changes for "parallax-tilt" update
      */
      // rotation angle
      tiltMaxAngleX={24}
      tiltMaxAngleY={24}
      // enlarge when hover
      /* scale={1.12} */
      transitionSpeed={200}
      // glare effects like reflection
      // maintain with card content
      // glareEnable={true}
      // glarePosition="all"
      // glareMaxOpacity={0.5}
      // glareBorderRadius="24px"
      // tiltReverse={true} // hover angle
      perspective={500}
      //
    >
      <motion.div
        variants={showVariants}
        className="w-full bg-slate-600 p-0.5 rounded-[20px] shadow-card"
      >
        {/* card content */}
        <motion.div
          variants={parallaxVariants}
          initial="rest"
          whileHover="hover"
          // original options params // options={{  }}
          className="bg-green-600 rounded-[20px] py-4 px-6 min-h-[280px] flex flex-col justify-center items-center drop-shadow"
        >
          <div
            style={{
              transform: "translateZ(100px)",
            }}
            className="para-context"
          >
            <h3 className="text-white ti-shadow text-[20px] text-center items-center font-bold">
              {title}
            </h3>
            context
            <li>1</li>
            <li>2</li>
          </div>
        </motion.div>
      </motion.div>
    </Tilt>
  );
};

export default AboutServiceTilt;
