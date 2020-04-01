// ~~~~~~ PARAMS ~~~~~~

base_diam = 25;
base_height = 3;
base_gap = 2;
upright_height = 30;
upright_length = 25;
upright_width = 2;
upright_to_centre = 18;
upright_to_upright = 2*upright_to_centre;
hole_diam = 3;
hole_space = 0.3;
base_to_hole = 24;
main_rod_extention = 5;
//distance rod extends from uprights


// ~~~~~~ BASE ~~~~~~

color(c="silver")
cylinder(base_height,base_diam,base_diam,$fa=1,$fs=1);

color(c="silver")
translate([0,0,base_gap+base_height])
cylinder(base_height,base_diam,base_diam,$fa=1,$fs=1);


// ~~~~~~ UPRIGHTS ~~~~~~

color(c="silver")
difference() {
    
    difference() {

        union() {
        
            translate([-upright_to_centre,0,2*base_height+base_gap])
            rotate([0,90,0])
            linear_extrude(upright_width)
            resize([upright_height*2, upright_length])circle(d=20,$fa=1,$fs=1);
            
            translate([upright_to_centre-upright_width,0,2*base_height+base_gap])
            rotate([0,90,0])
            linear_extrude(upright_width)
            resize([upright_height*2, upright_length])circle(d=20,$fa=1,$fs=1);
        }
        
        // ~~~~~~ UPRIGHT HOLES ~~~~~~
        
        translate([0,0,base_to_hole+2*base_height+base_gap])
        rotate([0,90,0])
        cylinder(2*base_diam,hole_diam,hole_diam,center=true);
        
    }
    
    // ~~~~~~ REMOVE LOWER UPRIGHT ~~~~~~
    
    translate([0,0,2*base_height+base_gap])
    rotate([180,0,0])
    cylinder(upright_height+1,base_diam,base_diam);
}


// ~~~~~~ MAIN ROD ~~~~~~

translate([0,0,base_to_hole+2*base_height+base_gap])
rotate([0,90,0])
cylinder(upright_to_upright+main_rod_extention,hole_diam-hole_space,hole_diam-hole_space,center=true,$fa=1,$fs=1);


// ~~~~~~ SIDE ROD (AMMO) ~~~~~~

translate([0,0,base_to_hole+2*base_height+base_gap])
rotate([-90,0,0])
cylinder(10,1,1,$fa=1,$fs=0.5);


// ~~~~~~ BOX HOLDER ~~~~~~

translate([-15/2,10,base_to_hole+2*base_height+base_gap-2])
linear_extrude(height=4)
polygon(points = [[0,0],[0,15],[15,15],[15,0],[1,1],[1,14],[14,14],[14,1]], paths = [[0,1,2,3],[4,5,6,7]]);


// ~~~~~~ SIDE ROD (TRIGGER) ~~~~~~

translate([0,0,base_to_hole+2*base_height+base_gap])
rotate([60,0,0])
cylinder(10,1,1,$fa=1,$fs=0.5);


// ~~~~~~ TRIGGER HOLDER ~~~~~~

out = 9;

translate([-out/2,-17,base_to_hole+2*base_height+base_gap+8])
rotate([-30,0,0])
linear_extrude(height=4)
polygon(points = [[0,0],[0,out],[out,out],[out,0],[1,1],[1,out-1],[out-1,out-1],[out-1,1]], paths = [[0,1,2,3],[4,5,6,7]]);


// ~~~~~~ RULER ~~~~~~

//rotate( [90, 0, 0] ) import("C:/Users/Lewis/Downloads/OpenSCAD_Ruler/OpenSCAD_Ruler/ruler.stl", convexity = 5);