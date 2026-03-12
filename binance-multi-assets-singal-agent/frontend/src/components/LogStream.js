import React, { useEffect, useRef } from 'react';

function LogStream({ messages }) {
  const logContainerRef = useRef(null);

  useEffect(() => {
    // 自動滾動到底部
    if (logContainerRef.current) {
      logContainerRef.current.scrollTop = logContainerRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div style={{ flex: 2, marginLeft: '20px' }}>
      <h2>Live Log</h2>
      <div
        ref={logContainerRef}
        style={{
          height: '400px',
          border: '1px solid #ccc',
          overflowY: 'scroll',
          padding: '10px',
          backgroundColor: '#f5f5f5',
          fontFamily: 'monospace',
          whiteSpace: 'pre-wrap',
        }}
      >
        {messages.map((msg, index) => (
          <div key={index}>{msg}</div>
        ))}
      </div>
    </div>
  );
}

export default LogStream;