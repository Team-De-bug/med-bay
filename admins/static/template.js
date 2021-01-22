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
        for (var i = 0; i < navItems.length; i++) {
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
    setTheme();    
    closeSidebar();

    if (sessionStorage.getItem('newSession') === null) {
        document.getElementById("loadLogoImg").style.opacity = "100%";
        setTimeout(function () { document.getElementById("loadLogoImg").style.opacity = "0"; }, 3000);
        setTimeout(function () {document.getElementById("loadLogo").style.opacity = "0"; }, 5000);
        setTimeout(function () {document.getElementById("loadLogo").style.display = "none"; }, 6000);
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

function toggleTheme() {

    var toggler = $('#theme-button');
    sessionStorage.setItem('toggle', 'true');
    if (sessionStorage.getItem('toggle') === 'true') {
        console.log("logo true")

        document.getElementById("loadLogo").style.display = "flex";
        setTimeout(function () {document.getElementById("loadLogo").style.opacity = "100%"; }, 100);
        setTimeout(function () { document.getElementById("loadLogoImg").style.opacity = "100%"; }, 500);

        setTimeout(function () { document.getElementById("loadLogoImg").style.opacity = "0"; }, 3000);
        setTimeout(function () {document.getElementById("loadLogo").style.opacity = "0"; }, 5000);
        setTimeout(function () {document.getElementById("loadLogo").style.display = "none"; }, 6000);
        sessionStorage.setItem('newSession', 'false');
    }

    setTimeout(function () {
        if (localStorage.getItem('theme') === 'light'){
            localStorage.setItem('theme', 'dark');
            $("link[rel=stylesheet]").attr("href", "/static/dark_theme.css");
            toggler.attr("src", "/static/images/light.png");
        } else if (localStorage.getItem('theme') === 'dark') {
            localStorage.setItem('theme', 'light');
            toggler.attr("src", "/static/images/dark.png");
            $("link[rel=stylesheet]").attr("href", "/static/style.css");
        } else if (localStorage.getItem('theme') === null) {
            localStorage.setItem('theme', 'light');
            toggler.attr("src", "/static/images/dark.png");
            $("link[rel=stylesheet]").attr("href", "/static/style.css");
            console.log("set default");
        }
    }, 1000);
}

function setTheme() {

    var toggler = $('#theme-button');

    if (localStorage.getItem('theme') === 'dark'){
        localStorage.setItem('theme', 'dark');
        $("link[rel=stylesheet]").attr("href", "/static/dark_theme.css");
        toggler.attr("src", "/static/images/light.png");
        console.log("set dark");
    } else if (localStorage.getItem('theme') === 'light') {
        localStorage.setItem('theme', 'light');
        toggler.attr("src", "/static/images/dark.png");
        $("link[rel=stylesheet]").attr("href", "/static/style.css");
        console.log("set light");
    } else if (localStorage.getItem('theme') === null) {
        localStorage.setItem('theme', 'light');
        toggler.attr("src", "/static/images/dark.png");
        $("link[rel=stylesheet]").attr("href", "/static/style.css");
        console.log("set default");
    }
}