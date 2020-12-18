var sidebarIsClosed = false;

function showLogo() {
    if (localStorage.getItem('first') == null) {
        document.getElementById("loadLogoImg").style.opacity = "100%";
        setTimeout(function () { document.getElementById("loadLogoImg").style.opacity = "0"; }, 3000);
        console.log("Logo gone");
        setTimeout(function () {document.getElementById("loadLogo").style.opacity = "0"; }, 5000);
        setTimeout(function () {document.getElementById("loadLogo").style.display = "none"; }, 7000);
        
        localStorage.setItem('first', 'false');
        
    } else {
        document.getElementById("loadLogo").style.display = "none";
    }
}

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
            navItems.item(i).style.opacity = "100%";
            navItems.item(i).style.fontSize = "1.5vw";
        }
        sidebarIsClosed = false;
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