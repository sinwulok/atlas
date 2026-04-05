import React, { useState, useEffect } from "react";

const Intro = () => {
  // sentence
  const sentences = [
    "over stack developer,",
    "include data process & database,",
    "researcher of machine learning and statistics algo etc.",
  ];
  const [text, setText] = useState("");
  const [index, setIndex] = useState(0);
  const [typing, setTyping] = useState(true);
  const [sentenceIndex, setSentenceIndex] = useState(0);

  useEffect(() => {
    if (sentenceIndex < sentences.length) {
      if (typing) {
        if (index < sentences[sentenceIndex].length) {
          setTimeout(() => {
            setText((prev) => prev + sentences[sentenceIndex].charAt(index));
            setIndex(index + 1);
          }, 150);
        } else {
          setTimeout(() => setTyping(false), 1500);
        }
      } else {
        if (index > 0) {
          setTimeout(() => {
            setText(sentences[sentenceIndex].substring(0, index - 1));
            setIndex(index - 1);
          }, 75);
        } else {
          setSentenceIndex(sentenceIndex + 1);
          setTyping(true);
        }
      }
    } else {
      // Display the full text after the last sentence is typed
      setText(sentences.join(" "));
    }
  }, [index, typing, sentenceIndex]);

  return <div>{text}</div>;
};

export default Intro;
