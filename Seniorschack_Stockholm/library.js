function changeMonth(month) { 
	history.replaceState(null, '', month); 
	window.location.reload();
} 
