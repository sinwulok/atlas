import React from "react";

import { styles } from "../styles";

import HeroWriter from "./HeroWritter";

import UseDviceSize from "./usehooks/UseDviceSize";
// import useHooks, params for desktopCanvas

import DesktopCanvas from "./canvas/Desktop";
import VendingCanvas from "./canvas/Vending";
import HeroIcons from "./HeroIcons";

import { isMobileSafari } from "react-device-detect";
// for safari

const Hero = () => {
  // pass param from useHooks
  // when def error check child component duplicate defined params
  const { isMobile, isTablet } = UseDviceSize();

  const NameTag = isMobile ? "div" : "span";

  return (
    /* Hero section */
    <section className="relative w-full h-screen mx-auto">
      {/* Hero main area */}
      <div
        className={`${styles.paddingX} absolute inset-0 top-[100px] lg:top-[110px] max-w-7xl mx-auto flex items-start gap-4`}
      >
        {/* liner icon */}
        <div className="flex flex-col justify-center items-center mt-5">
          <div className="w-5 h-5 rounded-full bg-violet-600" />
          <div className="w-1 sm:h-80 h-40 violet-gradient" />
        </div>

        {/* text content */}
        <div className="break-words">
          <h4 className={`${styles.heroHeadText} text-white`}>
            Hi, I am
            <NameTag className="text-orange-400"> Maximilian</NameTag>
          </h4>

          <p className={`${styles.heroSubText} mt-2 text-white`}>
            Working on
            <HeroWriter className={`sm:mx-auto text-violet-400`} />
          </p>
        </div>
      </div>

      {/*
       3d desktopPC/computer module
       this part can rotate or holding-move when users touch
       but limit by the 3D object area
      */}
      <VendingCanvas
        //
        isMobile={isMobile}
        isTablet={isTablet}
      />

      {/* Flowing bottom icons */}
      <HeroIcons
        isMobile={isMobile}
        isTablet={isTablet}
        browserCondition={isMobileSafari}
      />
    </section>
  );
};

export default Hero;
