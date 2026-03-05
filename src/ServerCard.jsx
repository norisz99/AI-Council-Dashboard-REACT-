// Fent a zárójelbe is bekerült a ram_load paraméter
function ServerCard({ name, status, load, ram_load }) {
  
  const statusColor = status === 'Online' ? '#28a745' : '#dc3545';

  return (
    <div style={{ 
      border: '1px solid #444', padding: '20px', margin: '10px', 
      borderRadius: '8px', backgroundColor: '#222', color: 'white', width: '300px'
    }}>
      <h3 style={{ marginTop: 0, color: '#61dafb' }}>🖥️ {name}</h3>
      <p>Állapot: <strong style={{ color: statusColor }}>{status}</strong></p>
      <p>CPU Terhelés: {load}%</p>
      <p>RAM Terhelés: {ram_load}%</p> {/* <--- EZ AZ ÚJ SOR */}
    </div>
  )
}

export default ServerCard