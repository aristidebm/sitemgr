import click
import re
import datetime


class URL(click.ParamType):
    """
    URL Validator Type.
    """

    def convert(self, value, param, ctx):
        pattern = re.compile(
            r"((http|https|ftp|smtp)://)(www.)?"
            + "[a-zA-Z0-9@:%._\\+~#?&//=]"
            + "{2,256}\\.[a-z]"
            + "{2,6}\\b([-a-zA-Z0-9@:%"
            + "._\\+~#?&//=]*)"
        )
        # check if value match url pattern otherwise raise an excpetion.
        try:
            if not isinstance(value, str):
                raise TypeError()
            elif not pattern.match(value):
                raise ValueError()
        except TypeError:
            error_message = f"expect string for URL conversion but got {value!r} of type {value.__class__.__name__}"
            self.fail(error_message, param, ctx)
        except ValueError:
            error_message = f"{value!r} is not valid {self.__class__.__name__} type."
            self.fail(error_message, param, ctx)

        return value


class TAG(click.ParamType):
    """
    Tag Field Validator.
    """

    def __init__(self):
        # the name of the class is used by to build the metavar: [CLASS_IN_UPPERCASE]
        # Example: -t, --tag TAG           Tag the site. TAG is the metavar
        # It isn't automatically done for option's custom type.
        self.name = self.__class__.__name__

    def convert(self, value, param, ctx):
        try:
            if not isinstance(value, str):
                raise TypeError()
            elif len(value) > 20:
                raise ValueError()
        except TypeError:
            error_message = f"expect string for Tag conversion but got {value!r} of type {value.__class__.__name__}"
            self.fail(error_message, param, ctx)
        except ValueError:
            error_message = f"{value!r} is not valid {self.__class__.__name__}. A tag contains at most 20 characters."
            self.fail(error_message, param, ctx)

        return value


class DATETIME(click.ParamType):
    # Input date format: 13 Dec 2020
    # Input date format: 2020 Dec 13
    def __init__(self):
        self.name = self.__class__.__name__

    def convert(self, value, param, ctx):
        pattern = re.compile(
            r"(\d{2}\s+[a-zA-z]{3}\s+\d{4})|(\d{4}\s+[a-zA-z]{3}\s+\d{2})"
        )
        months = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12,
        }
        value = value.strip()
        try:
            if not isinstance(value, str):
                raise TypeError()

            if pattern.match(value):
                value_list = value.split()
                # remove all surrounding spaces.
                for index, _ in enumerate(value_list):
                    value_list[index] = value_list[index].strip()
                value_list[1] = value_list[1].capitalize()

                # check if the input month is valid and change it with it integer value
                if value_list[1] in months.keys():
                    value_list[1] = str(months.get(value_list[1]))
                    # adapt the input date  to suite datetime.datetime(Year, Month, Day) format
                    if len(value_list[0]) == 2:
                        day = value_list[0]
                        value_list[0] = value_list[2]
                        value_list[2] = day

                        datetime.datetime(
                            int(value_list[0].strip()),
                            int(value_list[1].strip()),
                            int(value_list[2].strip()),
                        )
                        value = " ".join(value_list)
            else:
                raise ValueError()
        except TypeError as t:
            error_message = f"expect string for {self.__class__.__name__} conversion but got {value!r} of type {value.__class__.__name__}"
            self.fail(error_message, param, ctx)
        except ValueError as v:
            error_message = f"{value!r} is not valid {self.__class__.__name__} type."
            self.fail(error_message, param, ctx)

        return value


# Custom types
Url = URL()
Tag = TAG()
DateTime = DATETIME()
