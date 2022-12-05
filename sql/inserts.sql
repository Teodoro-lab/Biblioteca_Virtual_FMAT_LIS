INSERT INTO library_career(name)
VALUES ('ingenieria de software');

-- ESTRUCTURA DE DATOS

INSERT INTO library_semester(semester_number, career_id)
VALUES (1, 1);
INSERT INTO library_semester(semester_number, career_id)
VALUES (2, 1);
INSERT INTO library_semester(semester_number, career_id)
VALUES (3, 1);
INSERT INTO library_semester(semester_number, career_id)
VALUES (4, 1);
INSERT INTO library_semester(semester_number, career_id)
VALUES (5, 1);
INSERT INTO library_semester(semester_number, career_id)
VALUES (6, 1);
INSERT INTO library_semester(semester_number, career_id)
VALUES (7, 1);
INSERT INTO library_semester(semester_number, career_id)
VALUES (8, 1);
INSERT INTO library_semester(semester_number, career_id)
VALUES (9, 1);

INSERT INTO library_course(name, description, slug, semester_id)
VALUES ('algoritmos y estructuras de datos', 'la materia se encargar de enseñar los fundamentos de la cosntrucción de software a través de la creación de estructuras de datos y algoritmos', 'algoritmos-y-estructuras-de-datos', 1);

INSERT INTO library_unit(name, description, unit_num, course_id)
VALUES ('estructuras de datos en la vida cotidiana', 'la unidad se encarga de enseñar las estructuras de datos más comunes', 1, 1);


-- MATERIALES PARA ESTRUCTURA DE DATOS


-- ESTE SERÍA UN MATERIAL NORMAL
INSERT INTO library_material(title, description, unit_id, date_publisehd)
VALUES ('estructuras de datos-santos aguilera', 'este material es un libro que explica las estructuras de datos más comunes', 1, '2018-01-01');

-- PARA CREAR UN RESOURCE O EXERCISE SE DEBE CREAR UN MATERIAL Y LUEGO UN RESOURCE O EXERCISE
INSERT INTO library_resource(material_ptr_id, upload, type)
VALUES (1, 'http://www.google.com', 'Generic');

-- OTRO MATERIAL PARA CREAR UN EXERCISE
INSERT INTO library_material(title, description, unit_id, date_publisehd)
VALUES ('estructuras de datos-santos aguilera', 'este material es un libro que explica las estructuras de datos más comunes', 1, '2018-01-01');

INSERT INTO library_resource(material_ptr_id, upload, type)
VALUES (2, 'www.facebook.com', 'Exercise');

-- COMMENTS
INSERT INTO library_comment(email, comment)
VALUES ('teodawn.td@gmail.com', 'este material es muy bueno');
