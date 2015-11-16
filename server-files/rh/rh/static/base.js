//-----------------------------Supporting Functions-----------------
function getTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    var end = " AM";

    if (Number(h) > 12) {
        h = Number(h) - 12;
        end = " PM";
    }    
    if (Number(h) == 0) {
        h = 12;
    }
    if (Number(m) < 10) {
        m = "0" + m;
    }
    if (Number(s) < 10) {
        s = "0" + s;
    }
    var time = h + ":" + m + ":" + s + end;
    
    return time;
}

//---------------------------------Classes----------------------------
function Clock(){
    var self = this;
    self.time = ko.observable(getTime());
    self.tick = function() {
        self.time(getTime());
    };

    setInterval(self.tick, 1000);
}

//---------------------------------Model------------------------------
function BaseViewModel() {
    var self = this;

    self.clock = ko.observable(new Clock());
}

// Activates knockout.js
ko.applyBindings(new BaseViewModel(), document.getElementById('base_header'));