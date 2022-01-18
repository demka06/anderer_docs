from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import sqlite3
import json
import random
import inspect
x = 21


def write_msg(txt, vk, event, attach=None, keyboard=None, peer_id=None):
	print(type(event))
	print(event)
	
	if not inspect.isclass(event):
		if peer_id is None:
			peer_id = event.object.message["peer_id"]
		vk.messages.send(
				peer_id=peer_id,
				random_id=random.randint(-1000000, 1000000),
				message=txt,
				attachment=attach,
				keyboard=keyboard
				)


def get_names(user, vk):
	names = vk.users.get(user_ids=user)
	name = names[0]['first_name']
	last = names[0]["last_name"]
	return name, last


def main_page( ):
	keyboard = VkKeyboard(one_time=False, inline=False)
	keyboard.add_button('Имя', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "st_name"}))
	keyboard.add_button('Фамилия', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "nd_name"}))
	keyboard.add_button('Отчество', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "rd_name"}))
	keyboard.add_line( )
	keyboard.add_button('Биография', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "biogr"}))
	keyboard.add_button('Дата рождения', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "db"}))
	keyboard.add_button('Раса', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "race"}))
	keyboard.add_line( )
	keyboard.add_button('Отправить на проверку', color=VkKeyboardColor.NEGATIVE, payload=json.dumps({"key": "send"}))
	keyboard.add_button('Анкета', color=VkKeyboardColor.NEGATIVE, payload=json.dumps({"key": "profile"}))
	keyboard.add_line( )
	# keyboard.add_button('Назад', color=VkKeyboardColor.PRIMARY, payload=json.dumps({"key": "back_page"}))
	keyboard.add_button('Страница #2', color=VkKeyboardColor.PRIMARY, payload=json.dumps({"key": "next_page"}))
	keyboard = keyboard.get_keyboard( )
	return keyboard


def nd_page( ):
	keyboard = VkKeyboard(one_time=False, inline=False)
	keyboard.add_button('Направление', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "prof"}))
	keyboard.add_line( )
	keyboard.add_button('Цель вступления', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "target"}))
	keyboard.add_line( )
	keyboard.add_button('Стаж в манямирах', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "exp"}))
	keyboard.add_line( )
	keyboard.add_button('Назад', color=VkKeyboardColor.PRIMARY, payload=json.dumps({"key": "back_page"}))
	keyboard = keyboard.get_keyboard( )
	return keyboard


def races_page( ):
	keyboard = VkKeyboard(one_time=False, inline=True)
	keyboard.add_button('Людины', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "1"}))
	keyboard.add_button('Дериды', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "2"}))
	keyboard.add_line( )
	keyboard.add_button('Пустотные Легионы', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "3"}))
	keyboard.add_button('Вендиго', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "4"}))
	keyboard.add_line( )
	keyboard.add_button('Лана А\'йрон', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "5"}))
	keyboard.add_button('Дендроиды', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "6"}))
	keyboard.add_line( )
	keyboard.add_button('Корусы', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "7"}))
	keyboard.add_button('Креатосы', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "8"}))
	keyboard = keyboard.get_keyboard( )
	return keyboard


def prof_page( ):
	keyboard = VkKeyboard(one_time=False, inline=True)
	keyboard.add_button('Рейды/рипы/шпионаж', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"prof": "1"}))
	keyboard.add_line( )
	keyboard.add_button('РП', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"prof": "2"}))
	keyboard.add_line( )
	keyboard.add_button('Мемы/монтаж/рисование', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"prof": "3"}))
	keyboard = keyboard.get_keyboard( )
	return keyboard


def raid_page( ):
	keyboard = VkKeyboard(one_time=False, inline=False)
	keyboard.add_button('Направление', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "raid_prof"}))
	keyboard.add_button('Раскрытие', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "is_imp"}))
	keyboard.add_line( )
	keyboard.add_button('Стаж в Anderer Weg', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "and_exp"}))
	keyboard.add_line( )
	keyboard.add_button(
			'Опыт в рипах и рейдах', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "raid_exp"})
			)
	keyboard.add_line( )
	keyboard.add_button('На главную страницу', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "main_page"}))
	keyboard = keyboard.get_keyboard( )
	return keyboard


def raid_prof_page( ):
	keyboard = VkKeyboard(one_time=False, inline=True)
	keyboard.add_button('Рейды', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "1"}))
	keyboard.add_line( )
	keyboard.add_button('Рипество', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "2"}))
	keyboard.add_line( )
	keyboard.add_button('Рипество и рейды', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "3"}))
	keyboard = keyboard.get_keyboard( )
	return keyboard


def imp_page( ):
	keyboard = VkKeyboard(one_time=False, inline=True)
	keyboard.add_button('Да, раскрывали', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "1"}))
	keyboard.add_line( )
	keyboard.add_button('Нет, не раскрывали', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"val": "2"}))
	keyboard = keyboard.get_keyboard( )
	return keyboard


def moder(user_id):
	keyboard = VkKeyboard(one_time=False, inline=True)
	keyboard.add_button(
			'Принять', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "acc", "user_id": user_id})
			)
	keyboard.add_line( )
	keyboard.add_button(
			'Отклонить', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "rem", "user_id": user_id})
			)
	keyboard.add_line( )
	keyboard.add_button(
			'Заполнить по новой', color=VkKeyboardColor.POSITIVE, payload=json.dumps({"key": "rew", "user_id": user_id})
			)
	keyboard = keyboard.get_keyboard( )
	return keyboard


def error_page( ):
	keyboard = VkKeyboard(one_time=True, inline=True)
	keyboard.add_button('Моя анкета', color=VkKeyboardColor.POSITIVE, payload="form")
	keyboard = keyboard.get_keyboard( )
	return keyboard


def check(user_id):
	conn = sqlite3.connect("main.db")
	curs = conn.cursor( )
	curs.execute(f"SELECT id FROM users WHERE user_id = {user_id}")
	if curs.fetchone( ) is None:
		return True
	else:
		return False


class Pasport(object):
	def __init__(self, vk, event, vk_session):
		self.vk = vk
		self.event = event
		self.user_id = event.object.message["from_id"]
		self.peer_id = event.object.message["peer_id"]
		self.command = event.obj.message["text"].lower( )
		self.txt = event.obj.message["text"]
		self.vk_session = vk_session
		if "payload" in self.event.object.message.keys( ):
			self.payload = event.object.message["payload"]
		else:
			self.payload = None
	
	def greeting(self):
		if check(self.user_id):
			write_msg(
					"Привет! Чтобы получить паспорт, тебе нужно заполнить анкету, нажимая на кнопки.\nПосле заполнения нужно нажать на \"Отправить на проверку\"",
					self.vk, self.event, keyboard=main_page( )
					)
	
	def set_st_name(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 2 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Напишите желаемое имя", self.vk, self.event)
	
	def set_nd_name(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 3 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Напишите желаемую фамилию", self.vk, self.event)
	
	def set_rd_name(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 4 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Напишите желаемое отчество", self.vk, self.event)
	
	def set_biogr(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 5 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Напишите биографию своего персонажа (1,5к символов - максимум)", self.vk, self.event)
	
	def set_birh_date(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 6 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Напишите желаемый дату рождения в формате ДД.ММ.ГГГГ (01.01.2022)", self.vk, self.event)
	
	def set_race(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 7 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Выберите 1 расу:", self.vk, self.event, keyboard=races_page( ))
	
	def set_photo(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 8 WHERE user_id = {self.user_id}")
		conn.commit( )
	
	def next_page(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			curs.execute(f"UPDATE users SET last_page=2 WHERE user_id = {self.user_id}")
			conn.commit( )
			write_msg("#2 Страница", self.vk, self.event, keyboard=nd_page( ))
		else:
			curs.execute(f"UPDATE users SET last_page=2 WHERE user_id = {self.user_id}")
			conn.commit( )
			write_msg("#2 Страница", self.vk, self.event, keyboard=nd_page( ))
	
	def back_page(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id, last_page FROM users WHERE user_id = {self.user_id}")
		a = curs.fetchone( )
		if a is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			write_msg("Куда назад то?", self.vk, self.event)
		else:
			print(2)
			if a[1] == 2:
				print(3)
				curs.execute(f"UPDATE users SET last_page=1 WHERE user_id = {self.user_id}")
				conn.commit( )
				write_msg("#1 Страница", self.vk, self.event, keyboard=main_page( ))
	
	def set_prof(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 9 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Выберите направление: ", self.vk, self.event, keyboard=prof_page( ))
	
	def set_target(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 10 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Укажите цель вступления", self.vk, self.event)
	
	def set_exp(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 11 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Укажите стаж в манямирах", self.vk, self.event)
	
	def get_profile(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
			write_msg("У вас еще пустая, постарайтесь его заполнить :)", self.vk, self.event)
		else:
			curs.execute(
					f"SELECT id,from_id,g_st_name,g_nd_name,r_st_name,r_nd_name,date_of_bd,race,access,exp,prof,target, biogr FROM forms WHERE from_id = {self.user_id}"
					)
			res = curs.fetchone( )
			curs.execute(f"SELECT name FROM races WHERE id = {res[7]}")
			if res[7] != 0:
				race = curs.fetchone( )[0]
			else:
				race = "Не указана"
			status = ""
			if res[8] == 0:
				status = "Анкета еще не отправлена"
			elif res[8] == 1:
				status = "Анкета принята"
			elif res[8] == 2:
				status = "Анкета  отклонена"
			elif res[8] == 3:
				status = "Анкета требует корректировки"
			elif res[8] == 4:
				status = "Анкета находится на проверке"
			prof = ""
			if res[10] == 1:
				prof = "Рейды/рипы/шпионаж"
			elif res[10] == 2:
				prof = "РП"
			elif res[10] == 3:
				prof = "Мемы/монтаж/рисование"
			write_msg(
					f"""Реальные Имя/Фамилия: {res[4]} {res[5]}
Игровые Имя/Фамилия: {res[2]} {res[3]}
Раса: {race}
Дата рождения: {res[6]}
Биография: {res[12]}
Опыт в манямирах: {res[9]}
Направление: {prof}
Цель вступления: {res[11]}

Статус анкеты: {status}
			""", self.vk, self.event
					)
	
	def and_exp(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 30 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Укажите стаж в Anderer Weg с точностью до месяца", self.vk, self.event)
	
	def raid_exp(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 31 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Укажите стаж в сферах рейдов и рипов", self.vk, self.event)
	
	def is_imp(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 32 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg(
				"Вас раскрывали/вы святились на большие аудитории в данной сфере?\n!!! Если да, ниже привести данные о причине и аудитории !!!",
				self.vk, self.event, keyboard=imp_page( )
				)
	
	def raid_prof(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
		else:
			pass
		curs.execute(f"UPDATE users SET page = 33 WHERE user_id = {self.user_id}")
		conn.commit( )
		write_msg("Выберите направление (-я) ", self.vk, self.event, keyboard=raid_prof_page( ))
	
	def back_to_main(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			conn.commit( )
			write_msg("Неа ", self.vk, self.event)
		else:
			curs.execute(
					f"SELECT raid_prof, detected, det_info, raid_exp FROM forms WHERE from_id = {self.user_id}"
					)
			res = curs.fetchone( )
			curs.execute(f"SELECT page FROM users WHERE user_id = {self.user_id}")
			page = curs.fetchone( )[0]
			if res[0] != 0 and res[3] != "Не указано" and res[1] != 0:
				if res[2] != "Отсутствует" and res[1] == 1:
					if 30 <= page or 3 == page:
						write_msg("Страница #1", self.vk, self.event, keyboard=main_page( ))
						curs.execute(
								f"UPDATE users SET page = 1 WHERE user_id = {self.user_id}"
								)
						conn.commit( )
					else:
						write_msg("Неа ", self.vk, self.event)
				elif res[1] == 2:
					if 30 <= page or 3 == page:
						write_msg("Страница #1", self.vk, self.event, keyboard=main_page( ))
						curs.execute(
								f"UPDATE users SET page = 1 WHERE user_id = {self.user_id}"
								)
						conn.commit( )
					else:
						write_msg("Неа ", self.vk, self.event)
				else:
					write_msg("Сначала вы должны полностью заполнить анкету", self.vk, self.event)
			else:
				write_msg("Сначала вы должны полностью заполнить анкету", self.vk, self.event)
	
	def send_to_moder(self):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT id FROM forms WHERE from_id = {self.user_id}")
		if curs.fetchone( ) is None:
			curs.execute(f"INSERT INTO users (user_id) VALUES ({self.user_id})")
			curs.execute(
					f"INSERT INTO forms (from_id, r_st_name, r_nd_name) VALUES (?,?,?)",
					(self.user_id, get_names(self.user_id, self.vk)[0], get_names(self.user_id, self.vk)[1])
					)
			conn.commit( )
			write_msg(
					"Сначала заполни полностью анкету. Если отправишь ее незаполненной, то исправить ее сможешь только по решению Администрации",
					self.vk, self.event
					)
		else:
			curs.execute(f"SELECT * FROM forms WHERE from_id = {self.user_id}")
			res = curs.fetchone( )
			if res[8] != 1 or res[8] != 2 or res[8] != 4:
				det = ""
				if res[14] == 1:
					det = f"Да, раскрывали\nПричина: {res[15]}"
				elif res[14] == 2:
					det = "Нет, не раскрывали"
				raid_prof = ""
				if res[13] == 1:
					raid_prof = "Рейды"
				elif res[13] == 2:
					raid_prof = "Рипество"
				elif res[13] == 3:
					raid_prof = "Рейды и рипество"
				race = "Не указано"
				if res[7] != 0:
					curs.execute(f"SELECT name FROM races WHERE id = {res[7]}")
					race = curs.fetchone( )[0]
				if res[10] == 1:
					prof = "Рейды/рипы/шпионаж"
				elif res[10] == 2:
					prof = "РП"
				elif res[10] == 3:
					prof = "Мемы/монтаж/рисование"
				else:
					prof = "Не указано"
				if res[10] != 1:
					write_msg(
							f"""Пользователь: @id{self.user_id}
[ЛД-1]Фамилия и имя из ВК
>{res[4]} {res[5]}
[ЛД-2] Стаж в манямирках
>{res[9]}
[ЛД-3] Профиль вступления
>{prof}
[ЛД-4] Цель вступления
>{res[11]}

ИГРОВЫЕ ДАННЫЕ
[ИД-1] ФИО персонажа
>{res[2]} {res[3]} {res[18]}
[ИД-2] Раса
>{race}
[ИД-3] Краткая биография
>{res[12]}""", self.vk, self.event, keyboard=moder(self.user_id), peer_id=2e9 + x)
					curs.execute(f"UPDATE forms SET access=4 WHERE from_id={self.user_id}")
					conn.commit( )
					write_msg("Анкета отправлена на проверку!", event=self.event, vk=self.vk)
				else:
					write_msg(
							f"""Пользователь: @id{self.user_id}
[ЛД-1]Фамилия и имя из ВК
>{res[4]} {res[5]}
[ЛД-2] Стаж в манямирках
>{res[9]}
[ЛД-3] Профиль вступления
>{prof}
[ЛД-4] Цель вступления
>{res[11]}

ИГРОВЫЕ ДАННЫЕ
[ИД-1] ФИО персонажа
>{res[2]} {res[3]} {res[18]}
[ИД-2] Раса
>{race}
[ИД-3] Краткая биография
>{res[12]}

==============================================

> ДАННЫЕ для БОЕВОГО БЛОКА.

[ДББ-1] Направление:
>{raid_prof}

[ДББ-2] Вас раскрывали/вы святились на большие аудитории в данной сфере?:
>{det}

[ДББ-3] Стаж в Anderer Weg
>{res[17]}

[ДББ-4] Информацию о опыте в сферах рипов и рейдов.
>{res[16]}
			""", self.vk, self.event, keyboard=moder(self.user_id), peer_id=2e9 + x
							)
					curs.execute(f"UPDATE forms SET access=4 WHERE from_id={self.user_id}")
					conn.commit( )
					write_msg("Анкета отправлена на проверку!", event=self.event, vk=self.vk)
			else:
				write_msg("Вашей анкете уже выдан вердикт или же она на проверке", self.event, self.vk)
	
	def form_access(self, user_id):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT access FROM forms WHERE from_id = {user_id}")
		res = curs.fetchone( )
		if res is not None:
			if res[0] == 4:
				curs.execute(f"UPDATE forms SET access=1 WHERE from_id = {user_id}")
				conn.commit( )
				write_msg(f"Анкета @id{user_id} принята", self.vk, self.event)
				write_msg(
						f"Ваша анкета принята! Поздравляем!\nСкоро с вами свяжутся", self.vk, self.event,
						peer_id=user_id
						)
			else:
				write_msg(f"Эта анкета еще либо не отправлена на проверку, либо уже проверена", self.vk, self.event)
		else:
			write_msg(f"Данной анкеты не существует", self.vk, self.event)
	
	def rej_form(self, user_id):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT access FROM forms WHERE from_id = {user_id}")
		res = curs.fetchone( )
		if res is not None:
			if res[0] == 4:
				curs.execute(f"UPDATE forms SET access=2 WHERE from_id = {user_id}")
				conn.commit( )
				write_msg(f"Анкета @id{user_id} отклонена", self.vk, self.event)
				write_msg(f"Ваша анкета отклонена :(", self.vk, self.event, peer_id=user_id)
			else:
				write_msg(f"Эта анкета еще либо не отправлена на проверку, либо уже проверена", self.vk, self.event)
		else:
			write_msg(f"Данной анкеты не существует", self.vk, self.event)
	
	def rewrite_form(self, user_id):
		conn = sqlite3.connect("main.db")
		curs = conn.cursor( )
		curs.execute(f"SELECT access FROM forms WHERE from_id = {user_id}")
		res = curs.fetchone( )
		if res is not None:
			if res[0] == 4:
				curs.execute(f"UPDATE forms SET moder={self.user_id} WHERE from_id = {user_id}")
				curs.execute(f"UPDATE forms SET access=3 WHERE from_id = {user_id}")
				conn.commit( )
				curs.execute(f"UPDATE users SET check_user = {user_id} WHERE user_id = {self.user_id}")
				curs.execute(f"UPDATE users SET page = 40 WHERE user_id = {self.user_id}")
				conn.commit( )
				write_msg("Напишите свои замечания в таком формате:\n@id1234\n[Замечания]", self.vk, self.event)
			else:
				write_msg(f"Эта анкета еще либо не отправлена на проверку, либо уже проверена", self.vk, self.event)
		else:
			write_msg(f"Данной анкеты не существует", self.vk, self.event)
