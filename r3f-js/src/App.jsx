import { BrowserRouter } from "react-router-dom";

import {
  About,
  Contact,
  Experience,
  Feedbacks,
  Hero,
  Navbar,
  Tech,
  Works,
  StarsCanvas,
  LottieViewer,
} from "./components";

import ErrorBoundary from "./components/usehooks/ErrorBoundary";
// debug with R3F(react-three-fiber) canvas components

const App = () => {
  return (
    <BrowserRouter>
      <div className="relative z-0 bg-primary">
        <div className="bg-hero-pattern bg-cover bg-no-repeat bg-center">
          <Navbar />
          <Hero />
        </div>
        <About />
        <Experience />

        <Tech />
        <Works />
        <Feedbacks />
        <div className="relative z-0">
          {/*<Contact />
           */}{" "}
          <StarsCanvas />
        </div>
        {/* <LottieViewer /> */}
      </div>
    </BrowserRouter>
  );
};

export default App;
