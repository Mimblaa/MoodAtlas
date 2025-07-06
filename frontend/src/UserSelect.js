import React, { useEffect, useState } from "react";

function UserSelect({ onUserSelected }) {
  const [users, setUsers] = useState([]);
  const [username, setUsername] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/users")
      .then((res) => res.json())
      .then((data) => {
        setUsers(data);
        setLoading(false);
      })
      .catch((err) => {
        setError("Could not fetch users");
        setLoading(false);
      });
  }, []);

  const handleSelect = (e) => {
    const userId = e.target.value;
    const user = users.find((u) => u.id === parseInt(userId));
    if (user) onUserSelected(user);
  };

  const handleCreate = async (e) => {
    e.preventDefault();
    if (!username.trim()) return;
    try {
      const res = await fetch("http://localhost:8000/users", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username }),
      });
      if (!res.ok) {
        setError("Failed to create user. Please try again.");
        return;
      }
      const user = await res.json();
      setUsers((prev) => [...prev, user]);
      setUsername("");
      onUserSelected(user);
    } catch (err) {
      setError("An error occurred while creating the user.");
    }
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
        <input
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
