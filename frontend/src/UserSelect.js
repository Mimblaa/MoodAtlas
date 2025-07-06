import React, { useEffect, useState } from "react";

function UserSelect({ onUserSelected, apiUrl }) {
  const [users, setUsers] = useState([]);
  const [username, setUsername] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${apiUrl}/users`)
      .then((res) => res.json())
      .then((data) => {
        setUsers(data);
        setLoading(false);
      })
      .catch((err) => {
        setError("Could not fetch users");
        setLoading(false);
      });
  }, [apiUrl]);

  const handleSelect = (e) => {
    const userId = e.target.value;
    const user = users.find((u) => u.id === parseInt(userId));
    if (user) onUserSelected(user);
  };

  const handleCreate = async (e) => {
    e.preventDefault();
    if (!username.trim()) return;
    const res = await fetch(`${apiUrl}/users`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username }),
    });
    const user = await res.json();
    setUsers((prev) => [...prev, user]);
    setUsername("");
    onUserSelected(user);
  };

  if (loading) return <div>Loading users...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div style={{ marginBottom: "2rem" }}>
      <h2>Select User</h2>
      {users.length > 0 ? (
        <select onChange={handleSelect} defaultValue="">
          <option value="" disabled>
            -- Choose user --
          </option>
          {users.map((u) => (
            <option key={u.id} value={u.id}>
              {u.username}
            </option>
          ))}
        </select>
      ) : (
        <div>No users found. Create a new one below.</div>
      )}
      <form onSubmit={handleCreate} style={{ marginTop: "1rem" }}>
        <label htmlFor="new-username">Enter new username:</label>
        <input
          id="new-username"
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="New username"
        />
        <button type="submit">Create User</button>
      </form>
    </div>
  );
}

export default UserSelect;
