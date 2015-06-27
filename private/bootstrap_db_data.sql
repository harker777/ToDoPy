DELETE FROM `user`;
INSERT INTO `user`
  (`login`, `password`, `name`, `mail`)
VALUES
  ('harker777', 'harker', 'Iaroslav', 'harker6666@gmail.com'),
  ('asilence', 'silence', 'Alexandra', 'silence@3g.ua');

DELETE FROM `project`;
INSERT INTO `project`
  (`name`, `color`, `parent_id`, `user_id`)
VALUES
  ('home', 1, null, 1),
  ('work', 2, null, 1),
  ('home', 1, null, 2),
  ('work', 2, null, 2);

DELETE FROM `tag`;
INSERT INTO `tag`
  (`name`, `user_id`)
VALUES
  ('tag1I', 1),
  ('tag2I', 1),
  ('tag1A', 2),
  ('tag2A', 2);

DELETE FROM `task`;
INSERT INTO `task`
  (`name`, `project_id`, `time`,`deadline`,`priority`,`status`, `parent`)
VALUES
  ('task1I', 1, null, null, 4, 1, null),
  ('task2I', 1, null, null, 4, 1, null),
  ('task1I', 2, null, null, 4, 1, null),
  ('task2I', 2, null, null, 4, 1, null),
  ('task1A', 1, null, null, 4, 1, null),
  ('task2A', 1, null, null, 4, 1, null),
  ('task1A', 2, null, null, 4, 1, null),
  ('task2A', 2, null, null, 4, 1, null);

DELETE FROM `tasks_tags`;
INSERT INTO `tasks_tags`
  (`task_id`, `tag_id`)
VALUES
  (1, 1),
  (2, 1),
  (3, 2),
  (4, 2);

