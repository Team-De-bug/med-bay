import logo from './images/med-bay.png'
import menu from './images/menu.svg'
import user from './images/user.png'
import theme_d from './images/dark.png'
import theme_l from './images/light.png'
import './App.css'
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom"
import { useState } from 'react'

import Appointments from './views/Appointments'
import Login from './views/Login'
import Modal from './components/Modal/Modal'
import BlackOut from './components/BackOut/BlackOut'

function NavBar(props) {

    const {toggleSidebar} = props

    const [isDarkTheme, setIsDarkTheme] = useState(localStorage.getItem("isDarkTheme"))
    
    let getTheme = () => {
      return(isDarkTheme)
    }

    function setTheme(){
      setIsDarkTheme(!isDarkTheme)
      localStorage.setItem("isDarkTheme", isDarkTheme)
    }

  return (
    <div className="floating-bar" id="floating-bar">
    	<div className="nav-bar">
        	<button className="side-bar-btn" value="click" onClick={toggleSidebar}>
          		<img className="side-bar-btn-icon" src={menu} margin="0" height="100%" alt="menu"/>
        	</button>
			<div id="logo-div">
				<Link to="/"><img id="logo" src={logo} alt="med-bay logo"/></Link>
			</div>
			<div className="user-btns">
				<button className="user-btn" onClick={setTheme} title="Toggle Theme">
					<img id="theme-button" className="user-btn-img" src={ getTheme() ? theme_l : theme_d} alt="theme indicator"/>
				</button>
				<button className="user-btn">
					<Link to="/login">
						<img className="user-btn-img" title="You are not logged in" src={user} alt="user icon"/>
					</Link>
				</button>
			</div>
		</div>
    </div>
  )
}

function NavItem(props) {
  	const {name, target} = props

  	return(
  		<Link to={target}><li className="nav-item"><div className="nav-link">{name}</div></li></Link>
  	)
}

function SideBar(props) {

  	const { auth, toggle } = props

  	let navItems = () => {
		if (auth.staff.role === "d") {
		return(<>
			<a className="nav-link" href="{% url 'doctor:dashboard' %}"><li className="nav-item">Doctor's Dashboard</li></a>
			<a className="nav-link" href="{% url 'doctor:recover' %}"><li className="nav-item">Recover Unsaved Prescriptions</li></a>
			<a className="nav-link" href="{% url 'doctor:case_archive' %}"><li className="nav-item">Patient Archive</li></a>
		</>)
		} else if ( auth.staff.role === "p") {
		return(<>
			<a className="nav-link" href="{% url 'pharma:shop' %}"><li className="nav-item">Pharmacy</li></a>
			<a className="nav-link" href="{% url 'pharma:bill_archive' %}"><li className="nav-item">Bill Archive</li></a>
			<a className="nav-link" href="{% url 'pharma:order_prescription' %}"><li className="nav-item">Prescription Orders</li></a>
		</>)
		} else if (auth.staff.role === "a"){
		return(<>
			<a className="nav-link" href="{% url 'admins:attendance' %}"><li className="nav-item">Doctor Attendance</li></a>
			<a className="nav-link" href="{% url 'admins:list_patients' %}"><li className="nav-item">Patients List</li></a>
			<a className="nav-link" href="{% url 'admins:list_cases' %}"><li className="nav-item">Cases List</li></a>
			<a className="nav-link" href="{% url 'admins:create_patient' %}"><li className="nav-item">Create Patient</li></a>
			<a className="nav-link" href="{% url 'admins:create_case' %}"><li className="nav-item">Create Case</li></a>
		</>)
		}else if (auth.staff.role === "ac"){
		return(<>
			<a className="nav-link" href="{% url 'accounts:dashboard' %}"><li className="nav-item">Dashboard</li></a>
			<a className="nav-link" href="{% url 'accounts:entries' %}"><li className="nav-item">Chart Of Accounts</li></a>
		</>)
		}
  	}

  	return (<>
	  	<BlackOut id="side-bar" onClick={toggle}/>
		<div className="side-bar">
			<div className="side-bar-top">
				<button className="side-bar-btn" value="click" onClick={toggle}>
				<img className="side-bar-btn-icon" src={menu} margin="0" height="100%" alt="menu"/>
				</button>
				<label>Go to</label>
			</div>
			<ul id="nav-list">
				<NavItem name="Home" target="/" />
				{navItems()}
			</ul>
		</div>
	</>)
}

function Home(props) {
  	return(<Appointments/>)
}

function App() {

	if (localStorage.getItem("isDarkTheme") === null){
		localStorage.setItem("isDarkTheme", false)
	}

	const [sideBarOpen, setsideBarOpen] = useState(false)
	const [blackOutOpen, setBlackOutOpenOpen] = useState(false)

	let toggleSidebar = () => {
		let sideBar = document.querySelector(".side-bar")
		if(!sideBarOpen) {
		sideBar.setAttribute("style", "transform: translate(0)")
		} else {
		sideBar.setAttribute("style", "transform: translate(-100%)")
		}
		toggleBlackOut("black-out-side-bar")
		setsideBarOpen(!sideBarOpen)
		// return(sideBarOpen)
	}


	function toggleBlackOut(id) {
		const blackOut = document.querySelector(`#${id}`)
		if(!blackOutOpen){
			blackOut.setAttribute("style", "display: grid")
		} else {
			blackOut.setAttribute("style", "display: none")
		}
		setBlackOutOpenOpen(!blackOutOpen)
	}

	const auth = {
		staff: {
			role: "a"
		}
	}

  	return (
		<div className="App">
			<Router>
				{/* <div id="loadLogo"><img id="loadLogoImg" src="{%static 'images/med-bay.png'%}" alt="med-bay logo" /></div> */}
				<NavBar toggleSidebar={toggleSidebar}/>
				<SideBar auth={auth} toggleSidebar={toggleSidebar}/>
				{/* <Modal show={true} ok={true} title="Es">EEEEEEEEEEEEE</Modal> */}
				<div className="main">
					<Switch>
						<Route path="/login">
							<Login />
						</Route>
						<Route path="">
							<Home />
						</Route>
					</Switch>
				</div>
			</Router>
		</div>
	)
}

export default App
