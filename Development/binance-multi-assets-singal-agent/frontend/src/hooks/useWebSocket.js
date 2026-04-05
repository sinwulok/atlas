import { useState, useEffect, useRef } from 'react';

export const useWebSocket = (url) => {
  const [messages, setMessages] = useState([]);
  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket(url);
    ws.current.onopen = () => console.log('WebSocket Connected');
    ws.current.onclose = () => console.log('WebSocket Disconnected');

    ws.current.onmessage = (event) => {
      setMessages((prevMessages) => [...prevMessages, event.data]);
    };

    return () => {
      if (ws.current) {
        ws.current.close();
      }
    };
  }, [url]);

  return messages;
};