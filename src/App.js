import "./App.css";
import "chart.js/auto";
import React, { useEffect, useState } from "react";
import axios from "axios";
import { Pie } from "react-chartjs-2";

import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

function Dashboard() {
  const [data, setData] = useState({ productive: 0, unproductive: 0 ,neutral: 0});
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/weekly/")
    .then(res =>{
        console.log("API Response:", res.data);
        setData(res.data);
      })
      .catch(err => console.log("ERROR:", err));
    },
    []);

const chartData = {
  labels: ["Productive", "Unproductive", "Neutral"],
  datasets: [
    {
      label: "Time Usage",
      data: [data.productive, data.unproductive,data.neutral],
      backgroundColor: ["#0fe42c", "#ece921", "#ff0000"],
      borderWidth: 2,
      hoverOffset: 4
    },
  ],
};

  return (
    <div className="container mt-4">
      <h2 className="mb-4">📊 Weekly Productivity</h2>

      {/* Chart */}
      <div className="row">
        <div className="chart col-12 col-md-3 "> 
          <div style={{ height: "300px",padding: "10px"}}>
            <Pie data={chartData} 
            options={{ maintainAspectRatio: false }} />
          </div>
          <div className="card col-12 col-md-3">
          <div className="card-body">
            <h5 className="card-title">Neutral Time</h5>
            <p className="card-text">{data.neutral}</p>
          </div>
        </div>
        <div className="card col-12 col-md-3">
          <div className="card-body">
            <h5 className="card-title">Productive Time</h5>
            <p className="card-text">{data.productive}</p>
          </div>
        </div>
        <div className="card col-12 col-md-3">
          <div className="card-body">
            <h5 className="card-title">Unproductive Time</h5>
            <p className="card-text">{data.unproductive}</p>
          </div>
        </div>
      </div>
      </div>
      </div>
   
  );
}

export default Dashboard;
