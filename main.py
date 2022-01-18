import random
import sqlite3
import json
import traceback

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import pasport
import re
import os

token = str(os.environ.get("VK-TOKEN"))  # token group
group_id = str(os.environ.get("VK-GROUP"))  # ID group

vk_session = vk_api.VkApi(token=token)  # Обработка access_token
longpoll = VkBotLongPoll(vk_session, group_id)  # Данные для работы в сообществе
vk = vk_session.get_api( )  # да
# ------------[ VARIBLE ]------------

# _____________СЛОВАРИ______________

admins_id = [274868427, 547409675, 305284615]
thr_days = [9, 4, 6, 11]
# ------------[ COMMANDS ] ----------
while True:
	
	for event in longpoll.listen( ):
		try:
			if event.type == VkBotEventType.MESSAGE_NEW and event.object.message['from_id'] > 0:
				print(event)
				command = event.object.message["text"].lower( )
				cmd = event.object.message["text"]
				psp = pasport.Pasport(vk, event, vk_session)
				user_id = event.object.message['from_id']
				if event.object.message['peer_id'] == event.object.message['from_id']:
					psp.greeting( )
					if "payload" in event.object.message.keys( ):
						pd = json.loads(event.object.message["payload"])
						if "key" in pd.keys( ):
							pd = pd["key"]
							if pd == "st_name":
								psp.set_st_name( )
							elif pd == "nd_name":
								psp.set_nd_name( )
							elif pd == "rd_name":
								psp.set_rd_name( )
							elif pd == "biogr":
								psp.set_biogr( )
							elif pd == "db":
								psp.set_birh_date( )
							elif pd == "next_page":
								psp.next_page( )
							elif pd == "back_page":
								psp.back_page( )
							elif pd == "race":
								psp.set_race( )
							elif pd == "prof":
								psp.set_prof( )
							elif pd == "target":
								psp.set_target( )
							elif pd == "exp":
								psp.set_exp( )
							elif pd == "db":
								psp.set_birh_date( )
							elif pd == "profile":
								psp.get_profile( )
							elif pd == "raid_prof":
								psp.raid_prof( )
							elif pd == "is_imp":
								psp.is_imp( )
							elif pd == "and_exp":
								psp.and_exp( )
							elif pd == "raid_exp":
								psp.raid_exp( )
							elif pd == "main_page":
								psp.back_to_main( )
							elif pd == "send":
								psp.send_to_moder( )
					
					conn = sqlite3.connect("main.db")
					curs = conn.cursor( )
					curs.execute(f"SELECT page FROM users WHERE user_id = {event.object.message['from_id']}")
					res = curs.fetchone( )
					if res is not None:
						# установка имени
						if "payload" not in event.object.message.keys( ):
							if res[0] == 2:
								if 30 >= len(cmd) >= 2:
									if cmd.isalpha( ):
										curs.execute(
												f"UPDATE forms SET g_st_name = ? WHERE from_id = {event.object.message['from_id']}",
												(command.capitalize( ),)
												)
										curs.execute(
												f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
												)
										conn.commit( )
										pasport.write_msg(
											"Установлено указанное вами имя!", vk, event, pasport.main_page( )
											)
									else:
										pasport.write_msg(
												"Имя может содержать в себе только буквы.\nПопробуйте ввести имя повторно",
												vk,
												event
												)
								else:
									pasport.write_msg(
											"Имя не может быть короче 2 символов или длиннее 30 символов.\nПопробуйте ввести имя повторно",
											vk, event
											)
							elif res[0] == 3:
								if 30 >= len(cmd) >= 2:
									if cmd.isalpha( ):
										curs.execute(
												f"UPDATE forms SET g_nd_name = ? WHERE from_id = {event.object.message['from_id']}",
												(command.capitalize( ),)
												)
										curs.execute(
												f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
												)
										conn.commit( )
										pasport.write_msg(
												"Установлена указанная вами фамилия!", vk, event, pasport.main_page( )
												)
									else:
										pasport.write_msg(
												"Фамилия может содержать в себе только буквы.\nПопробуйте ввести фамилию повторно",
												vk, event
												)
								else:
									pasport.write_msg(
											"Фамилия не может быть короче 2 символов или длиннее 30 символов.\nПопробуйте ввести фамилию повторно",
											vk, event
											)
							elif res[0] == 4:
								if 15 >= len(cmd) >= 2:
									if cmd.isalpha( ):
										curs.execute(
												f"UPDATE forms SET g_rd_name = ? WHERE from_id = {event.object.message['from_id']}",
												(cmd,)
												)
										curs.execute(
												f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
												)
										conn.commit( )
										pasport.write_msg(
												"Установлено указанное вами отчество!", vk, event, pasport.main_page( )
												)
									else:
										pasport.write_msg(
												"Отчество может содержать в себе только буквы.\nПопробуйте ввести отчество повторно",
												vk, event
												)
								else:
									pasport.write_msg(
											"Отчество не может быть короче 2 символов или длиннее 15 символов.\nПопробуйте ввести отчество повторно",
											vk, event
											)
							
							elif res[0] == 6:
								if re.match("\d{1,2}.\d{1,2}.\d{4}", cmd):
									if 3000 >= int(cmd.split(".")[2]) >= 0:
										if 12 >= int(cmd.split(".")[1]) >= 1:
											if int(cmd.split(".")[1]) == 2:
												if 29 >= int(cmd.split(".")[0]) >= 1:
													if int(cmd.split(".")[2]) % 4 == 0:
														curs.execute(
																f"UPDATE forms SET date_of_birh = ? WHERE from_id = {event.object.message['from_id']}",
																(cmd,)
																)
														curs.execute(
																f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
																)
														conn.commit( )
														pasport.write_msg(
															"Вы указали желаемую дату рождения", vk, event
															)
													else:
														pasport.write_msg(
																"Этот год не високосный, значит в феврале нет 29 дней :)\nПопробуйте указать дату еще раз",
																vk, event
																)
												else:
													pasport.write_msg(
															"Нулевого дня не существует :)\nПопробуйте указать дату еще раз",
															vk,
															event
															)
											else:
												if 31 >= int(cmd.split(".")[0]) >= 1:
													if int(cmd.split(".")[0]) == 31:
														if int(cmd.split(".")[1]) not in thr_days:
															curs.execute(
																	f"UPDATE forms SET date_of_birh = ? WHERE from_id = {event.object.message['from_id']}",
																	(cmd,)
																	)
															curs.execute(
																	f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
																	)
															conn.commit( )
															pasport.write_msg(
																"Вы указали желаемую дату рождения", vk, event
																)
														else:
															pasport.write_msg(
																	"В этом месяце только 30 дней :)\nПопробуйте указать дату еще раз",
																	vk, event
																	)
													else:
														curs.execute(
																f"UPDATE forms SET date_of_bd = ? WHERE from_id = {event.object.message['from_id']}",
																(cmd,)
																)
														curs.execute(
																f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
																)
														conn.commit( )
														pasport.write_msg(
															"Вы указали желаемую дату рождения", vk, event
															)
												else:
													pasport.write_msg(
															"Нулевого дня не существует :)\nПопробуйте указать дату еще раз",
															vk,
															event
															)
										else:
											pasport.write_msg(
													"В году только 12 месяцев :(\nПопробуйте указать дату еще раз", vk,
													event
													)
									else:
										pasport.write_msg(
												"Вы можете указать год от 0 до 3000 :(\nПопробуйте указать дату еще раз",
												vk,
												event
												)
								else:
									pasport.write_msg(
											"Вы указали неверный формат даты, либо указали не дату вообще :(\nПопробуйте указать дату еще раз",
											vk, event
											)
							if res[0] == 10:
								if 50 >= len(cmd) >= 10:
									curs.execute(
											f"UPDATE forms SET target = ? WHERE from_id = {event.object.message['from_id']}",
											(cmd,)
											)
									curs.execute(
											f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
											)
									conn.commit( )
									pasport.write_msg("Вы указали цель вступления", vk, event)
								else:
									pasport.write_msg(
											"Цель вступления не может быть длиннее 50 символов :(\nПопробуйте указать цель еще раз",
											vk, event
											)
							elif res[0] == 11:
								if 15 >= len(cmd) >= 5:
									curs.execute(
											f"UPDATE forms SET exp = ? WHERE from_id = {event.object.message['from_id']}",
											(cmd,)
											)
									curs.execute(
											f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
											)
									conn.commit( )
									pasport.write_msg("Вы указали стаж в манямирах", vk, event)
								else:
									pasport.write_msg(
											"Стаж не может быть длиннее 15 символов :(\nПопробуйте указать стаж еще раз",
											vk, event
											)
							elif res[0] == 5:
								if 1500 >= len(cmd) >= 2:
									curs.execute(
											f"UPDATE forms SET biogr = ? WHERE from_id = {event.object.message['from_id']}",
											(cmd,)
											)
									curs.execute(
											f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
											)
									conn.commit( )
									pasport.write_msg("Вы указали биографию своего персонажа", vk, event)
								else:
									pasport.write_msg(
											"Биография не может быть длиннее 1,5к символов :(\nПопробуйте указать биографию еще раз",
											vk, event
											)
							elif res[0] == 34:
								if 80 >= len(cmd) >= 2:
									curs.execute(
											f"UPDATE forms SET det_info = ? WHERE from_id = {event.object.message['from_id']}",
											(cmd,)
											)
									curs.execute(
											f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
											)
									conn.commit( )
									pasport.write_msg("Вы указали информацию о причинах и о аудитории", vk, event)
								else:
									pasport.write_msg(
											"Попробуйте уложиться в 80 символов",
											vk, event
											)
							elif res[0] == 30:
								if 20 >= len(cmd) >= 2:
									curs.execute(
											f"UPDATE forms SET and_exp = ? WHERE from_id = {event.object.message['from_id']}",
											(cmd,)
											)
									curs.execute(
											f"UPDATE users SET page = 3 WHERE user_id = {event.object.message['from_id']}"
											)
									conn.commit( )
									pasport.write_msg("Вы указали стаж в Anderer Weg", vk, event)
								else:
									pasport.write_msg(
											"Попробуйте уложиться в 20 символов",
											vk, event
											)
							elif res[0] == 31:
								if 20 >= len(cmd) >= 2:
									curs.execute(
											f"UPDATE forms SET raid_exp = ? WHERE from_id = {event.object.message['from_id']}",
											(cmd,)
											)
									curs.execute(
											f"UPDATE users SET page = 3 WHERE user_id = {event.object.message['from_id']}"
											)
									conn.commit( )
									pasport.write_msg("Вы указали стаж в редах/рипах", vk, event)
								else:
									pasport.write_msg(
											"Попробуйте уложиться в 20 символов",
											vk, event
											)
						else:
							pd = json.loads(event.object.message["payload"])
							if "val" in pd.keys( ):
								if res[0] == 7:
									if 8 >= int(pd["val"]) >= 1:
										curs.execute(
												f"UPDATE forms SET race = {pd['val']} WHERE from_id = {event.object.message['from_id']}"
												)
										curs.execute(
												f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
												)
										conn.commit( )
										pasport.write_msg("Вы указали желаемую расу", vk, event)
									else:
										pasport.write_msg("Кого наебать хочешь?", vk, event)
								elif res[0] == 33:
									if 3 >= int(pd["val"]) >= 1:
										curs.execute(
												f"UPDATE forms SET raid_prof = {pd['val']} WHERE from_id = {event.object.message['from_id']}"
												)
										curs.execute(
												f"UPDATE users SET page = 3 WHERE user_id = {event.object.message['from_id']}"
												)
										conn.commit( )
										pasport.write_msg("Вы указали желаемое направление", vk, event)
									else:
										pasport.write_msg("Кого наебать хочешь?", vk, event)
								elif res[0] == 32:
									if 2 >= int(pd["val"]) >= 1:
										curs.execute(
												f"UPDATE forms SET detected = {pd['val']} WHERE from_id = {event.object.message['from_id']}"
												)
										if int(pd["val"]) == 1:
											curs.execute(
													f"UPDATE users SET page = 34 WHERE user_id = {event.object.message['from_id']}"
													)
											pasport.write_msg(
													"Хорошо. Теперь укажите информация о причине и аудитории, на которой вы засветились",
													vk, event
													)
										else:
											curs.execute(
													f"UPDATE users SET page = 3 WHERE user_id = {event.object.message['from_id']}"
													)
											pasport.write_msg("Хорошо", vk, event)
										conn.commit( )
							if "prof" in pd.keys( ):
								if res[0] == 9:
									if 3 >= int(pd["prof"]) >= 1:
										if pd["prof"] == "1":
											curs.execute(
													f"UPDATE forms SET prof = {pd['prof']} WHERE from_id = {event.object.message['from_id']}"
													)
											conn.commit( )
											pasport.write_msg(
												"Вам придется указать еще кое-что", vk, event,
												keyboard=pasport.raid_page( )
												)
										else:
											curs.execute(
													f"UPDATE forms SET prof = {pd['prof']} WHERE from_id = {event.object.message['from_id']}"
													)
											curs.execute(
													f"UPDATE users SET page = 1 WHERE user_id = {event.object.message['from_id']}"
													)
											conn.commit( )
											pasport.write_msg("Вы указали желаемое направление", vk, event)
									else:
										pasport.write_msg("Кого наебать хочешь?", vk, event)
				else:
					if pasport.x + 2e9 == event.object.message["peer_id"]:
						if "payload" in event.object.message.keys( ):
							pd = json.loads(event.object.message["payload"])
							if "key" in pd.keys( ):
								if pd["key"] == "acc":
									psp.form_access(pd["user_id"])
								elif pd["key"] == "rem":
									psp.rej_form(pd["user_id"])
								elif pd["key"] == "rew":
									psp.rewrite_form(pd["user_id"])
						
						else:
							conn = sqlite3.connect("main.db")
							curs = conn.cursor( )
							curs.execute(f"SELECT page FROM users WHERE user_id = {event.object.message['from_id']}")
							res = curs.fetchone( )
							if res is not None:
								if res[0] == 40:
									if len(cmd) <= 100:
										data = cmd.split("\n", 1)
										user = int(data[0].split("|")[0].replace("[id", ""))
										pasport.write_msg(
											f"Анкета на требует коррекции.\nЗамечания Администрации:\n{data[1]}", vk,
											event, peer_id=user
											)
										curs.execute(f"UPDATE users SET page = 1 WHERE user_id =  {user_id}")
										conn.commit( )
										pasport.write_msg("Замечания отправлены.", vk, event)
									else:
										pasport.write_msg("Попробуйте уложиться в 100 символов", vk, event)
		except Exception:
			vk.messages.send(
					peer_id=2e9 + 4,
					random_id=random.randint(0, 10000000000),
					message=f"[ERROR]\n{traceback.format_exc( )}\n\nLAST_EVENT: {event}"
					)
			print(traceback.format_exc( ))
