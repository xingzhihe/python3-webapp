drop database if exists awesome;

create database awesome;

use awesome;

grant select, insert, update, delete on awesome.* to 'etlusr'@'localhost' identified by 'etlusr';

create table users (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table blogs (
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `name` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table comments (
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table datasources (
    `id` varchar(50) not null,
    `db_type` varchar(10) not null,
    `host` varchar(50) not null,
    `port` int not null,
    `database` varchar(50) not null,
    `user` varchar(50) not null,
    `password` varchar(50) not null,
    `options` varchar(500) null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;


INSERT INTO `users` (`id`, `email`, `passwd`, `admin`, `name`, `image`, `created_at`) VALUES('001538901417388a03570925af44f84b556ccbc8919b99d000','aa@163.com','169a6a1acb9f9d6a78634036ecb5c162943cebdb','1','aa','about:blank','1538901417.38854');
