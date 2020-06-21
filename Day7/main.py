def my_print(txt): 
	print(txt)

msg_template = """ Hello {name}, Thanks for joining {website}

"""

def format_msg(name="Jusin", website="asdf"):
	my_msg = msg_template.format(name=name, website=website)
	# print(my_msg)
	return my_msg