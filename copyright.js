var copyright = function(company = '') {
	var eles= document.getElementsByClassName('copyright');
	for(i = 0; i < eles.length; i++) {
   		now = new Date;
   		currentYear=now.getYear();
   		if(currentYear < 1900) { currentYear = currentYear + 1900;};
    	eles[i].innerHTML = `&copy; ${company} ${currentYear}`
	}
}