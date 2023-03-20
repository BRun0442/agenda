create database agenda;
use agenda;

create table contatos(
	id int primary key auto_increment not null,
    nome varchar(250) not null,
    email varchar(250) not null,
    telefone varchar(14) not null,
    tipoTelefone enum('residencial', 'celular', 'nao informado')
);

insert into contatos(nome, email, telefone, tipoTelefone) 
	values('Osmiro', 'brunoosmar442@gmail.com', '05511910922910', 'celular');
    
select * from contatos;