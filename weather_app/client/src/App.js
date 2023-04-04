import React, {useState, useEffect} from 'react'
import axios from 'axios'

function App() {

  const [data, setData] = useState([{}])

  useEffect(() =>
    axios.get("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  )



  return (
    <div>
      {(typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ): (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}
    </div>
  );
}

export default App;
