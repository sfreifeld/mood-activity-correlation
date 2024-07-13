
import './App.css'
import React, { useState, useEffect } from 'react';

function App() {
  const [activityData, setActivityData] = useState(null);

  useEffect(() => {
    fetch('/activity-data?code=YOUR_AUTH_CODE_HERE')  // Make sure to replace 'YOUR_AUTH_CODE_HERE' with the actual code
        .then(response => response.json())
        .then(data => setActivityData(data))
        .catch(error => console.error('Error fetching activity data:', error));
}, []);


return (
  <div>
      <h1>Fitbit Activity Data</h1>
      {activityData ? (
          <pre>{JSON.stringify(activityData, null, 2)}</pre>
      ) : (
          <p>Loading activity data...</p>
      )}
  </div>
);
}

export default App
