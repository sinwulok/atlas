import React, { useState, useEffect } from 'react';
import BotController from './BotController';
import LogStream from './LogStream';
import AssetStatus from './AssetStatus';
import { getBotStatus } from '../api/botApi';
import { useWebSocket } from '../hooks/useWebSocket';

function Dashboard() {
  const [status, setStatus] = useState({ is_running: false, positions: {} });
  const logMessages = useWebSocket('ws://localhost:8000/ws/logs');

  const fetchStatus = async () => {
    try {
      const response = await getBotStatus();
      setStatus(response.data);
    } catch (error) {
      console.error('Failed to fetch bot status', error);
    }
  };

  useEffect(() => {
    // 初始載入時獲取一次狀態
    fetchStatus();
    // 每 5 秒輪詢一次狀態
    const interval = setInterval(fetchStatus, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ fontFamily: 'sans-serif', padding: '20px' }}>
      <h1>Binance Trading Bot Dashboard</h1>
      <BotController isRunning={status.is_running} onStatusChange={fetchStatus} />
      <div style={{ display: 'flex', marginTop: '20px' }}>
        <AssetStatus positions={status.positions} />
        <LogStream messages={logMessages} />
      </div>
    </div>
  );
}

export default Dashboard;