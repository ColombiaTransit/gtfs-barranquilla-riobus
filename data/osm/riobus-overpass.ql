[out:json][timeout:90];
/*
 RíoBus Karakalí: Puerta de Oro / Gran Malecón to Puerto Mocho.
 Bounding box: south,west,north,east.
 Search only relevant river infrastructure and named features.
*/
(
  nwr["man_made"="pier"](10.98,-74.85,11.10,-74.72);
  nwr["amenity"="ferry_terminal"](10.98,-74.85,11.10,-74.72);
  nwr["waterway"="dock"](10.98,-74.85,11.10,-74.72);
  nwr["waterway"="fairway"](10.98,-74.85,11.10,-74.72);
  nwr["route"="ferry"](10.98,-74.85,11.10,-74.72);
  nwr["name"~"Karakal[ií]|R[ií]o.?Bus|Puerta de Oro|Puerto Mocho|Intendencia Fluvial|Los Tramposos|Las Compa[nñ][ií]as",i](10.98,-74.85,11.10,-74.72);
);
out body center geom;
