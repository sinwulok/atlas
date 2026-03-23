import React from "react";

const neuronsIframe = () => {
  return (
    <div className="sketchfab-embed-wrapper flex justify-center items-center mt-5">
      <iframe
        title="Neurons"
        frameBorder="0"
        allowFullScreen
        mozallowfullscreen="true"
        webkitallowfullscreen="true"
        allow="autoplay; fullscreen; xr-spatial-tracking"
        xr-spatial-tracking
        execution-while-out-of-viewport
        execution-while-not-rendered
        web-share
        src="https://sketchfab.com/models/20e930a5fae5457fa6d1738afa00c7bb/embed"
      ></iframe>
      <p
        style={{
          fontSize: "13px",
          fontWeight: "normal",
          margin: "5px",
          color: "#4A4A4A",
        }}
      >
        <a
          href="https://sketchfab.com/3d-models/neurons-20e930a5fae5457fa6d1738afa00c7bb?utm_medium=embed&utm_campaign=share-popup&utm_content=20e930a5fae5457fa6d1738afa00c7bb"
          target="_blank"
          rel="noopener noreferrer"
          style={{ fontWeight: "bold", color: "#1CAAD9" }}
        >
          Neurons
        </a>
        by
        <a
          href="https://sketchfab.com/guillemfont?utm_medium=embed&utm_campaign=share-popup&utm_content=20e930a5fae5457fa6d1738afa00c7bb"
          target="_blank"
          rel="noopener noreferrer"
          style={{ fontWeight: "bold", color: "#1CAAD9" }}
        >
          Guillem Font
        </a>
        on
        <a
          href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=20e930a5fae5457fa6d1738afa00c7bb"
          target="_blank"
          rel="noopener noreferrer"
          style={{ fontWeight: "bold", color: "#1CAAD9" }}
        >
          Sketchfab
        </a>
      </p>
    </div>
  );
};

export default neuronsIframe;
