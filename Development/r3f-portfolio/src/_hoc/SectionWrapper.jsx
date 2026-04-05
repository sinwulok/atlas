import React, { useState } from "react";
import { motion } from "framer-motion";

import { styles } from "../styles";
import { staggerContainer } from "../utils/motion";
// motion variants customerize

// import { useInView } from "react-intersection-observer";
// depuca

/* 
  wrap all child components with same animate contorl
*/
const SectionWrapper = (Component, idName) =>
  function HOC() {
    const [animateComplete, setAnimateComplete] = useState(false);

    return (
      <motion.section
        /* motion build-in properties */
        variants={staggerContainer()} // apply animate
        initial="hidden"
        whileInView="show"
        viewport={{ once: false, amount: 0.2 }} // amount to 30% screen view
        onAnimationComplete={() => setAnimateComplete(true)} // turn on glare effects
        className={`${styles.padding} max-w-7xl mx-auto relative z-0`}
      >
        <span className="hash-span" id={idName}>
          &nbsp;
        </span>

        <Component
          animateComplete={animateComplete} // pass state
        />
      </motion.section>
    );
  };

export default SectionWrapper;
