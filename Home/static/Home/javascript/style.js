$(document).ready(function(){
    $('.control-menu img').click(function(){
        let width_menu_left = $(':root').css('--width-menu-left');
        if(width_menu_left=='15%'){
            width_menu_left = '73px';
            $('.content-icon-left').css('display','none');
        }
        else{
            width_menu_left = '15%';
            $('.content-icon-left').css('display','inline');
        }
        $(':root').css('--width-menu-left',width_menu_left);
    });
});