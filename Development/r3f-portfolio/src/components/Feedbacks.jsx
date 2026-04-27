import React from "react";
import { testimonials } from "../constants";

const Feedbacks = () => {
  return (
    <div className="py-10 px-4 max-w-3xl mx-auto">
      <h2 className="text-2xl font-bold mb-6 text-center">Feedbacks</h2>
      <div className="space-y-6">
        {testimonials.map((item, idx) => (
          <div key={idx} className="bg-tertiary rounded-xl p-6 shadow-md flex items-center gap-4">
            <img src={item.image} alt={item.name} className="w-14 h-14 rounded-full object-cover border-2 border-primary" />
            <div>
              <p className="text-lg mb-1">"{item.testimonial}"</p>
              <div className="text-sm text-secondary">
                — {item.name}，{item.designation} @ {item.company}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Feedbacks;
