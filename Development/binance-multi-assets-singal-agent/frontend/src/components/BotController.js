import React from 'react';
import { startBot, stopBot } from '../api/botApi';

function BotController({ isRunning, onStatusChange }) {
  const handleStart = async () => {
    await startBot();
    onStatusChange();
  };

  const handleStop = async () => {
    await stopBot();
    onStatusChange();
  };

  return (
    <div>
      <h2>Bot Control</h2>
      <p>Status: {isRunning ? <span style={{color: 'green'}}>Running</span> : <span style={{color: 'red'}}>Stopped</span>}</p>
      <button onClick={handleStart} disabled={isRunning}>Start Bot</button>
      <button onClick={handleStop} disabled={!isRunning} style={{marginLeft: '10px'}}>Stop Bot</button>
    </div>
  );
}

export default BotController;