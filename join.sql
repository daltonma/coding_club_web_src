SELECT artist.stage_name, `group`.name FROM artist JOIN `group` ON artist.group_id = `group`.id WHERE `group`.name = 'SEVENTEEN';
