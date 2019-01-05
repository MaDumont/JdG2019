#!/usr/bin/env escript

check(Line, Sub) ->
        Contains = string:str(Line, Sub),
	case Contains of
	     0 -> nil;
	     _ -> io:fwrite(Line), io:fwrite("\n") end,
	main([Sub]).
	
main([Sub]) ->
	Input = io:get_line(""),
	Empty = case Input of eof -> true; _ -> string:is_empty(Input) end,
	if Empty -> ok;
	   true -> check(string:trim(Input), Sub) end.