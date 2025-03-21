<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SkillSync</title>
    <style>
        /* General Styles */
        body {
            background: linear-gradient(to right, #a8c0ff, #3f2b96);
            color: #ffffff;
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
            transition: opacity 0.5s;
        }

        /* Navbar */
        .navbar {
            backdrop-filter: blur(30px);
            box-shadow: 0 0 30px rgba(227,228,237,0.37);
            border: 2px solid rgba(255, 255, 255, 0.18);
            width: 100%;
            background-color: rgba(255, 255, 255, 0.2);
            position: fixed;
            top: 0;
            left: 0;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            padding: 15px 30px;
            align-items: center;
        }

        .navbar a {
            color: white;
            text-decoration: none;
            margin: 0 10px;
        }

        .navbar a:hover {
            text-decoration: underline;
        }

        .search-bar {
            flex-grow: 1;
            margin: 0 20px;
        }

        .search-bar input {
            width: 100%;
            padding: 10px;
            border: 2px solid rgba(255, 255, 255, 0.5);
            border-radius: 10px;
            background-color: transparent;
            color: white;
            font-size: 16px;
        }

        .search-bar input::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }

        /* Main Container */
        .main-container {
            margin-top: 150px;
            padding: 20px;
            gap: 20px;
            max-width: 1200px;
            margin: auto;
            display: flex;
        }

        /* Profile Section */
        .profile-section {
            width: 30%;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        }

        .profile-icon {
            width: 100px;
            height: 100px;
            background: #ccc;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #3f2b96;
            font-size: 3rem;
            margin-bottom: 20px;
        }

        .profile-details {
            text-align: center;
        }

        .profile-box {
            background-color: rgba(255,255,255,0.2);
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
        }

        /* Main Content */
        .main-content {
            width: 70%;
            text-align: left;
        }

        .recommended-profile {
            background-color: rgba(255, 255, 255, 0.3);
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
        }

        .recommended-profile:hover {
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }

        /* Login and Sign Up Page Styles */
        .login-container, .signup-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: calc(100vh - 120px);
        }

        .login-box, .signup-box {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
            width: 400px;
        }

        input {
            background-color: transparent;
            border: 2px solid rgba(255, 255, 255, 0.5);
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            width: calc(100% - 30px);
            color: white;
            font-size: 16px;
        }

        input::placeholder {
            color: rgba(255, 255, 255, 0.7);
        }

        button {
            width: calc(100% - 30px);
            padding: 10px;
            background-color: #3f2b96;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background-color: #5a4e9a;
        }

        /* Links */
        .link {
            color: rgba(255, 255, 255, 0.8);
            text-decoration: none;
            cursor: pointer;
        }

        .link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<!-- Sign Up Page -->
<div id="signup-page" class="signup-container">
    <div class="signup-box">
        <h1>Sign Up</h1>
        <form id="signup-form">
            <input type="text" id="signup-name" placeholder="Name" required>
            <input type="text" id="signup-skills" placeholder="Skills" required>
            <input type="text" id="signup-certifications" placeholder="Certifications" required>
            <input type="text" id="signup-highlights" placeholder="Highlights" required>
            <input type="text" id="signup-languages" placeholder="Languages" required>
            <input type="text" id="signup-skills-interested" placeholder="Skills Interested to Learn" required>
            <input type="password" id="signup-password" placeholder="Password" required>
            <button type="submit">Sign Up</button>
            <p>Already have an account? <a class="link" onclick="showPage('login')">Login</a></p>
        </form>
    </div>
</div>

<!-- Login Page -->
<div id="login-page" class="login-container" style="display:none;">
    <div class="login-box">
        <h1>Login</h1>
        <form id="login-form">
            <input type="text" id="login-name" placeholder="Name" required>
            <input type="password" id="login-password" placeholder="Password" required>
            <button type="submit">Login</button>
            <p>Don't have an account? <a class="link" onclick="showPage('signup')">Sign Up</a></p>
        </form>
    </div>
</div>

<!-- Home Page -->
<div id="home-page" style="display:none;">
    <div class="navbar">
        <a href="#" onclick="showPage('home')">Home</a>
        <div class="search-bar">
            <input type="text" id="search-input" placeholder="Search profiles by name or skills...">
        </div>
        <a href="#" id="logout-link">Logout</a>
    </div>

    <div class="main-container">
        <!-- Profile Section -->
        <div class="profile-section">
            <div class="profile-icon">👤</div>
            <div class="profile-details">
                <h2 id="profile-name"></h2>
                <p><strong>Skills:</strong> <span id="profile-skills"></span></p>
                <p><strong>Certifications:</strong> <span id="profile-certifications"></span></p>
                <p><strong>Highlights:</strong> <span id="profile-highlights"></span></p>
                <p><strong>Languages:</strong> <span id="profile-languages"></span></p>
                <p><strong>Skills Interested to Learn:</strong> <span id="profile-skills-interested"></span></p>
            </div>
        </div>

        <!-- Main Content -->
        <div class="main-content">
            <h1>Recommended Profiles</h1>
            <div id="recommended-profiles">
                <!-- Recommended profiles will be dynamically added here -->
            </div>
        </div>
    </div>
</div>

<script>
    // Mock Database
    let users = [];

    // Sample Recommended Profiles
    const recommendedProfiles = [
        { name: "John Doe", skills: "JavaScript", description: "Looking for someone to teach JavaScript!" },
        { name: "Jane Smith", skills: "Python", description: "I can teach Python. Let's connect!" },
        { name: "Emily Johnson", skills: "React.js", description: "Interested in learning React.js." },
        { name: "Michael Brown", skills: "Data Science", description: "Offering mentorship in Data Science." },
    ];

    // Function to render recommended profiles
    function renderRecommendedProfiles(filteredProfiles = recommendedProfiles) {
        const profilesContainer = document.getElementById("recommended-profiles");
        profilesContainer.innerHTML = ""; // Clear existing content

        filteredProfiles.forEach(profile => {
            const profileDiv = document.createElement("div");
            profileDiv.className = "recommended-profile";
            profileDiv.innerHTML = `
                <h3>${profile.name}</h3>
                <p>${profile.description}</p>
            `;
            profilesContainer.appendChild(profileDiv);
        });
    }

    // Search Functionality
    document.getElementById("search-input").addEventListener("input", function (e) {
        const searchTerm = e.target.value.toLowerCase();
        const filteredProfiles = recommendedProfiles.filter(profile =>
            profile.name.toLowerCase().includes(searchTerm) ||
            profile.skills.toLowerCase().includes(searchTerm)
        );
        renderRecommendedProfiles(filteredProfiles);
    });

    // Sign Up Functionality
    document.getElementById("signup-form").addEventListener("submit", function (e) {
        e.preventDefault();
        const name = document.getElementById("signup-name").value.trim();
        const skills = document.getElementById("signup-skills").value.trim();
        const certifications = document.getElementById("signup-certifications").value.trim();
        const highlights = document.getElementById("signup-highlights").value.trim();
        const languages = document.getElementById("signup-languages").value.trim();
        const skillsInterested = document.getElementById("signup-skills-interested").value.trim();
        const password = document.getElementById("signup-password").value.trim();

        if (name && skills && certifications && highlights && languages && skillsInterested && password) {
            const newUser = { name, skills, certifications, highlights, languages, skillsInterested, password };
            users.push(newUser);
            localStorage.setItem("users", JSON.stringify(users));
            alert("Sign up successful! Please login.");
            showPage('login');
        } else {
            alert("Please fill in all fields.");
        }
    });

    // Login Functionality
    document.getElementById("login-form").addEventListener("submit", function (e) {
        e.preventDefault();
        const name = document.getElementById("login-name").value.trim();
        const password = document.getElementById("login-password").value.trim();

        const storedUsers = JSON.parse(localStorage.getItem("users")) || [];
        const user = storedUsers.find(u => u.name === name && u.password === password);

        if (user) {
            localStorage.setItem("currentUser", JSON.stringify(user));
            showPage('home');
        } else {
            alert("Invalid credentials. Please try again.");
        }
    });

    // Logout Functionality
    document.getElementById("logout-link").addEventListener("click", function () {
        localStorage.removeItem("currentUser");
        showPage('login');
    });

    // Show Page Function
    function showPage(page) {
        document.body.style.opacity = "0";
        setTimeout(() => {
            document.getElementById("signup-page").style.display = (page === "signup") ? "flex" : "none";
            document.getElementById("login-page").style.display = (page === "login") ? "flex" : "none";
            document.getElementById("home-page").style.display = (page === "home") ? "block" : "none";

            if (page === "home") {
                loadProfile();
                renderRecommendedProfiles(); // Render profiles on home page load
            }

            document.body.style.opacity = "1";
        }, 500);
    }

    // Load Profile Function
    function loadProfile() {
        const currentUser = JSON.parse(localStorage.getItem("currentUser"));
        if (currentUser) {
            document.getElementById("profile-name").innerText = currentUser.name || "";
            document.getElementById("profile-skills").innerText = currentUser.skills || "";
            document.getElementById("profile-certifications").innerText = currentUser.certifications || "";
            document.getElementById("profile-highlights").innerText = currentUser.highlights || "";
            document.getElementById("profile-languages").innerText = currentUser.languages || "";
            document.getElementById("profile-skills-interested").innerText = currentUser.skillsInterested || "";
        }
    }

    // On Load
    window.onload = () => {
        const currentUser = JSON.parse(localStorage.getItem("currentUser"));
        showPage(currentUser ? "home" : "login");
    };
</script>
</body>
</html>
