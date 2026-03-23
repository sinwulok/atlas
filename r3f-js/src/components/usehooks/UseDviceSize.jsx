// useDviceSize.js
import { useState, useEffect } from "react";

function UseDviceSize() {
  // useState hook for mobile re-scale
  const [isMobile, setIsMobile] = useState(false);
  const [isTablet, setIsTablet] = useState(false);

  useEffect(() => {
    // set the query check screen width
    const mobileQuery = window.matchMedia("(max-width: 644px)");
    const tabletQuery = window.matchMedia(
      "(min-width: 744px) and (max-width: 1080px)"
    );

    // when matches = True, else = false (default as false)
    const handleMobileQueryChange = (event) => {
      setIsMobile(event.matches); // when event changes the prop updates
    };

    const handleTabletQueryChange = (event) => {
      setIsTablet(event.matches);
    };

    // callback function update isMobile state changes
    mobileQuery.addEventListener("change", handleMobileQueryChange);
    tabletQuery.addEventListener("change", handleTabletQueryChange);

    // Set the initial value
    setIsMobile(mobileQuery.matches);
    setIsTablet(tabletQuery.matches);

    // cleanup when unmounted
    return () => {
      mobileQuery.removeEventListener("change", handleMobileQueryChange);
      tabletQuery.removeEventListener("change", handleTabletQueryChange);
    };
  }, []);

  return { isMobile, isTablet };
}

export default UseDviceSize;
