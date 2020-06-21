msg_template = """ Hello {name}, Thanks for joining {website}

"""

def format_msg(name="Jusin", website="asdf"):
	my_msg = msg_template.format(name=name, website=website)
	return my_msg