def lazy_scribe(sources: list):
    # W tym zadaniu wcielisz się w skrybe (a do tego lenia i plagiatora) ciągów znakowych.
    # Skryba dostał zadanie stworzenia nowego ciągu znakowego. Nie chce mu się poświęcać
    # na to zbyt dużo czasu więc postanowił wykorzystać ciągi znakowe ze swojej biblioteczki.
    # 
    # Skryba działa metodycznie i chce całkowicie wykorzystać potencjał swojej kolekcji ciągów.
    # Wypracował następujący schemat działania:
    # 1. Bierze pierwszy ciąg z bilioteczki
    # 2. Przepisuje pierwszy znak z pobranego z bilbioteczki ciągu do ciągu, który właśnie tworzy
    # 3. Zapamiętuje, że wykorzystał już pierwszy znak z pierwszego ciągu
    # 4. Przechodzi do kolejnego ciągu, wybiera go zgodnie z kolejnościa przechowywania ciągów w
    #    biblioteczce
    # 5. Kopiuje z pobranego ciągu pierwszy znak, którego jeszcze nie wykorzystał z danego ciągu i
    #    i zapamiętuje który znak wykorzystał
    # 6. Powtarza kroki 4 i 5, jeśli dojdzie do końca bilbioteczki to wraca na jej początek i powtarza
    #    proces tak długo, aż wykorzysta wszystkie znaki ze wszystkich dostępnych w bilbioteczce ciągów
    # 
    # Dodatkowo z racji tego, że jest leniwy, kompresuje w tworzonym ciągu powtarzające się znaki
    # zastępując je liczbą kolejnych wystąpień tego samego znaku połączoną z samym znakiem
    # np. "aaaaaaa" -> "7a"
    #
    # Przykład:
    # Skryba ma w swojej bilbioteczce (`sources`) następujące ciągi znakowe:
    # `sources = ["python", "java", "golang"]`
    #
    # Jego genialna i nowatorska metoda tworzenia nowych ciogów zaowocuje następującym ciągiem:
    # `result = "pjgyaotvlh2ao2ng"`
    #  
    # Pomóż skrybie zautomatyzowac ten proces! Rezultat przypisz do zmiennej `result`.

    # * W liście `sources` znajdują się ciągi znakowe które odpowiadają bilbioteczce skryby.
    # * Ciągi znakowe w 'sources' składają się wyłącznie ze znaków a-z.
    # * Znaki traktuj jako unikalne podmioty, wykorzystanie znaku 'a' z któregoś z ciągów z
    #   z biblioteczki nie oznacza, że nie można wykorzystać znaku 'a' znajdującego się
    #   dalej w tym samym ciągu

    # wszystkie stringi tej samej dlugosci
    if len(sources) == 0:
        return ''
    elif len(sources) == 1:
        return sources[0]

    string_lengths = [len(s) for s in sources]
    longest_length: int = max(string_lengths)

    if longest_length == 0:
        return ''

    sources_with_fixed_length = [s + '' * (longest_length - len(s)) for s in sources]

    # polączenie stringów i usunięcie spacji
    interweaving_string = ''

    for chars in zip(*sources_with_fixed_length):
        interweaving_string += ''.join(chars)

    interweaving_string = interweaving_string.replace(' ', '')

    # zebranie wyniku
    result: str = ''
    current_char = interweaving_string[0]
    current_counter = 0

    for char in interweaving_string[1:]:
        if char == current_char:
            current_counter += 1
            continue

        if current_counter == 0:
            result += current_char
            current_char = char
        else:
            result += (str(current_counter + 1) + current_char)
            current_counter = 0
            current_char = char

    if current_counter == 0:
        result += current_char
    else:
        result += (str(current_counter + 1) + current_char)

    return result
