$(function(){
    var catagory="";
    var searchBy="";
    $('.sortby').click(function(){
        if($(this).text() == "Reset"){
            $('.sorttoggle').html("Sort By"+ "<span class='caret'></span>");
        }
        else{
            $('.sorttoggle').html("Sorted By: " + $(this).text()+ "<span class='caret'></span>");
        }

        searchBy = $(this).text();

        if(searchBy == "Price"){
            searchBy="P";
        }
        else if(searchBy == "A-Z"){
            searchBy="A";
        }
        else if(searchBy == "Manufacture Date"){
            searchBy="D";
        }
        else{
            searchBy=""
        }
        console.log(searchBy);
        $('.content').html('').load("/ajaxSearch/?search=" + encodeURIComponent($('#searchbar').val()) + "&catagory=" + catagory + "&by=" + searchBy);

    });

    $('.navCat').click(function(){
        $('.navCat').parent().removeClass("active");
        $(this).parent().addClass("active");

        catagory = $(this).text();

        if(catagory == "Agricultural Products"){
            catagory="L";
        }
        else if(catagory == "Machineries"){
            catagory="M";
        }
        console.log(catagory);
        console.log(searchBy);
        $('.content').html('').load("/ajaxSearch/?search=" + encodeURIComponent($('#searchbar').val()) + "&catagory=" + catagory + "&by=" + searchBy);
    });

    $("#searchForm").on('submit',function(event){
        event.preventDefault();
    });

    $("#searchbar").keyup(function(){
        $('.content').html('').load("/ajaxSearch/?search=" + encodeURIComponent($(this).val()) + "&catagory=" + catagory + "&by=" + searchBy);
    });

    $('.showdiv').click(function(){
        $('.warranty').toggleClass('hidden');
    });

});
