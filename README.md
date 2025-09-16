# Flask + React Demo Project

A full-stack web application demonstrating the integration between a Flask backend API and a React frontend.

## 🏗️ Project Structure

```
flask-demo1/
├── Flask_server/          # Backend API server
│   ├── server.py         # Main Flask application
│   └── venv/             # Python virtual environment
└── client/               # Frontend React application
    ├── src/
    │   ├── App.js        # Main React component
    │   └── index.js      # React entry point
    ├── package.json      # Node.js dependencies
    └── public/           # Static assets
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 
- Node.js 14+
- npm or yarn

### Backend Setup (Flask Server)

1. **Navigate to Flask server directory:**
   ```bash
   cd Flask_server
   ```

2. **Activate virtual environment:**
   ```bash
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Start the Flask server:**
   ```bash
   python server.py
   ```
   
   The server will run on `http://localhost:5000`

### Frontend Setup (React Client)

1. **Navigate to client directory:**
   ```bash
   cd client
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the React development server:**
   ```bash
   npm start
   ```
   
   The app will run on `http://localhost:3001`

## 🔧 How It Works

### Backend (Flask)
- **Framework:** Flask with CORS enabled
- **Port:** 5000
- **API Endpoint:** `/members`
- **Response:** JSON with array of member names

```python
@app.route('/members')
def members():
    return jsonify({"members": ["members1", "members2", "members3"]})
```

### Frontend (React)
- **Framework:** React 19.1.1
- **Port:** 3001 (configured in package.json)
- **Proxy:** Automatically proxies API calls to Flask server
- **Data Fetching:** Uses `fetch()` API to get data from `/members` endpoint

```javascript
useEffect(() => {
  fetch('/members')
    .then(response => response.json())
    .then(data => setData(data.members));
}, []);
```

### Communication Flow
1. React app makes a request to `/members`
2. Due to proxy configuration, request goes to `http://localhost:5000/members`
3. Flask server responds with JSON data
4. React displays the member names in the UI

## 🛠️ Key Technologies

### Backend
- **Flask:** Lightweight Python web framework
- **Flask-CORS:** Handles Cross-Origin Resource Sharing
- **Python Virtual Environment:** Isolated dependency management

### Frontend
- **React:** JavaScript library for building user interfaces
- **React Scripts:** Development tools and build configuration
- **Fetch API:** Modern way to make HTTP requests

## 📋 Available Scripts

### Backend
- `python server.py` - Start Flask development server

### Frontend
- `npm start` - Start React development server
- `npm build` - Build for production
- `npm test` - Run tests
- `npm eject` - Eject from Create React App

## 🌐 Access Points

- **Frontend:** http://localhost:3001
- **Backend API:** http://localhost:5000
- **API Endpoint:** http://localhost:5000/members

## 🔍 Troubleshooting

### Common Issues

1. **"Cannot fetch data" error:**
   - Ensure Flask server is running on port 5000
   - Check that virtual environment is activated
   - Verify CORS is enabled in Flask

2. **Port conflicts:**
   - Flask runs on port 5000
   - React runs on port 3001
   - Check if ports are available: `lsof -i :5000` or `lsof -i :3001`

3. **Dependencies not found:**
   - Backend: Ensure virtual environment is activated
   - Frontend: Run `npm install` in client directory

### Verification Steps

1. **Test Flask API directly:**
   ```bash
   curl http://localhost:5000/members
   ```
   Should return: `{"members": ["members1", "members2", "members3"]}`

2. **Check React app:**
   - Open http://localhost:3001
   - Should display three member names
   - Check browser console for any errors

## 🎯 Project Goals

This demo showcases:
- **Full-stack integration** between Python backend and React frontend
- **API communication** using modern fetch API
- **Development workflow** with hot reloading
- **CORS handling** for cross-origin requests
- **Virtual environment** best practices

## 👥 Team Presentation Notes

### Key Points to Highlight
1. **Separation of Concerns:** Backend handles data, frontend handles UI
2. **Modern Development:** Hot reloading, development servers
3. **API Design:** RESTful endpoint structure
4. **Dependency Management:** Virtual environments and package.json
5. **Cross-Origin Support:** CORS configuration for API access

### Demo Flow
1. Show Flask server running and API endpoint working
2. Demonstrate React app fetching and displaying data
3. Explain the proxy configuration
4. Show how changes in either server reflect immediately
5. Highlight the clean separation between frontend and backend

---

**Happy coding! 🚀**
