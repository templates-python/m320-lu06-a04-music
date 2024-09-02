from main import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Max spielt mit Gitarre den Ton a\nMoritz spielt mit Klavier den Ton f\n'