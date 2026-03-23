import { motion } from "framer-motion";
import { mouse } from "../assets";

const HeroIcons = ({ isMobile, isTablet, browserCondition }) => {
  // const { isMobile, isTablet } = UseDviceSize();
  // debug when use as single component.

  // def base class for icon positioning
  const baseIconBarClass = "absolute flex w-full justify-center items-center";

  const baseIconCenter = "flex justify-center";

  // browser position adjustment for Safari
  const conditionPosition = browserCondition
    ? "xs:bottom-12 bottom-28 mb-1"
    : "xs:bottom-6 lg:bottom-4 bottom-14 mb-2";

  // re-size for the scroll icon
  const scrollIconSize =
    isMobile || isTablet ? "w-[26px] h-[42px] " : "w-[34px] h-[64px] p-2";

  // re-size for scroll dot
  const scrollIconDotSize = isMobile || isTablet ? "w-2 h-2" : "w-3 h-3";

  // function visibility of the mouse icon
  const mouseIconVisibility = isMobile
    ? "hidden"
    : isTablet
    ? "w-[44px] h-[44px]"
    : "w-[64px] h-[64px]";

  return (
    /* base icon bar */
    <div className={`${baseIconBarClass} ${conditionPosition} z-10`}>
      {/* scroll button */}
      <a
        href="#about"
        className={`${baseIconCenter} items-center text-violet-400 text-sm`}
      >
        {/* scroll button notice text */}
        {isMobile && (
          <div className="absolute w-[144px] flex justify-around underline  hover:decoration-2 font-bold">
            <span>Click</span>
            <span></span>
            <span>me !</span>
          </div>
        )}
        {/* scroll icon */}
        <div
          className={`${scrollIconSize} ${baseIconCenter} rounded-3xl border-4 border-secondary items-start`}
        >
          <motion.div
            animate={{
              y: [0, 24, 0],
            }}
            transition={{
              duration: 2,
              repeat: Infinity,
              repeatType: "loop",
            }}
            className={`${scrollIconDotSize} rounded-full bg-secondary mb-1`}
          />
        </div>
      </a>

      {/* mouse-icon */}
      <div className={`${mouseIconVisibility} absolute bottom-0 right-0`}>
        <img src={mouse} alt="mouse" className="object-contain" />
      </div>
    </div>
  );
};

export default HeroIcons;
