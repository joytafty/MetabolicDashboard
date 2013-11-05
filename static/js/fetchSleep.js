var sleep = $.getJSON("data.json", function (d) {
	var items = [];
    $.each(d, function(p,v) {
    	slscore = v.efficiency;                
        console.log(slscore);
    })
});