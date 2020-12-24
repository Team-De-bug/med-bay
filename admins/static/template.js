var sidebarIsClosed = false;

var xhttp = new XMLHttpRequest();

function closeSidebar() {
    var navItems = document.getElementsByClassName("nav-link");
    //if the sidebar is not closed
    if (!sidebarIsClosed) {
        //then we close the sidebar
        document.getElementById('floating-bar').setAttribute("style", "grid-template-columns: 0% auto");
        document.getElementById('root-grid').setAttribute("style", "grid-template-columns: 0% auto");
        document.getElementById('side-bar-title').style.opacity = "0%";
        document.getElementById('side-bar-title').style.fontSize = "0vw";
        for (i = 0; i < navItems.length; i++) {
            navItems.item(i).style.opacity = "0%";
            navItems.item(i).style.fontSize = "0vw";
        }
        sidebarIsClosed = true;
    } else {
        //we open the sidebar
        document.getElementById('floating-bar').setAttribute("style", "grid-template-columns: 18% auto");
        document.getElementById('root-grid').setAttribute("style", "grid-template-columns: 18% auto");
        document.getElementById('side-bar-title').style.opacity = "100%";
        document.getElementById('side-bar-title').style.fontSize = "1.75vw";
        for (i = 0; i < navItems.length; i++) {
            navItems.item(i).style.display = "block";
            navItems.item(i).style.opacity = "100%";
            navItems.item(i).style.fontSize = "1.5vw";
        }
        sidebarIsClosed = false;
    }
}

function showLogo() {
    
    closeSidebar();
    
    if (sessionStorage.getItem('newSession') === null) {
        document.getElementById("loadLogoImg").style.opacity = "100%";
        setTimeout(function () { document.getElementById("loadLogoImg").style.opacity = "0"; }, 3000);
        console.log("Logo gone");
        setTimeout(function () {document.getElementById("loadLogo").style.opacity = "0"; }, 5000);
        setTimeout(function () {document.getElementById("loadLogo").style.display = "none"; }, 7000);
        
        sessionStorage.setItem('newSession', 'false');
        
    } else {
        document.getElementById("loadLogo").style.display = "none";
    }
}

function showMessage(message) {
    alert(message);
}

function copyDetail(detailId) {
    var copyID = document.getElementById(detailId);
    copyID.select();
    copyID.setSelectionRange(0, 99999)
    document.execCommand("copy");
    showMessage("Copied Pateint Detail: " + copyID.value);
}

function showPatientFull(patientId) {
    
    var patients = document.getElementsByClassName("patient-black-out");
    
    for (i = 0; i < patients.length; i++) {
        if (patients.item(i).id == patientId) {
            patients.item(i).style.display="flex";
        }
    }
    
}

function closePatientFull() {
    var patients = document.getElementsByClassName("patient-black-out");
    
    for (i = 0; i < patients.length; i++) {
            patients.item(i).style.display = "none";

    }
}