def play(mani, process, firstCardOnLeft=True, verbose=False, fast=True):

    mazzo_giocatore_uno, mazzo_giocatore_due = mani  # mani are called mazzo_giocatore_uno and mazzo_giocatore_due
    mazzo_iniziale_giocatore_uno = mazzo_giocatore_uno
    mazzo_iniziale_giocatore_due = mazzo_giocatore_due
    if not fast:
        print(process, "-", "Mani iniziali: ", mani)
    if not firstCardOnLeft:
        mazzo_giocatore_uno.reverse()
        mazzo_giocatore_due.reverse()
    mazzo_in_tavola = []  # cards in the middle
    turni = 0
    prese = 0
    #inizializzo: cominicia dal primo mazzo
    giocatore_corrente = 1  # alternates between 1 and -1
    while len(mazzo_giocatore_uno) != 0 and len(mazzo_giocatore_due) != 0:  # game terminates when mazzo_giocatore_uno or mazzo_giocatore_due's mani are empty
        partita_in_corso = False
        carte_da_buttare_nel_mazzo = 1
        while carte_da_buttare_nel_mazzo > 0:  # current giocatore_corrente may play up to carte_da_buttare_nel_mazzo cards
            turni += 1

            try:
                if giocatore_corrente == 1:
                    # grab next card from first character of string mazzo_giocatore_uno
                    prossima_carta = mazzo_giocatore_uno[0]
                    mazzo_giocatore_uno = mazzo_giocatore_uno[1:]
                else:
                    # grab next card from first character of string mazzo_giocatore_due
                    prossima_carta = mazzo_giocatore_due[0]
                    mazzo_giocatore_due = mazzo_giocatore_due[1:]
            except IndexError:
                break  # ran out of cards to play, game over...

            mazzo_in_tavola.append(prossima_carta)  # add to the mazzo_in_tavola
            #aggiungo stampa del mazzo in tavola
            # print("Mazzo corrente : ",mazzo_in_tavola)
            if prossima_carta == 0:
                # not a court card
                if partita_in_corso:
                    # this giocatore_corrente needs keep trying to find a court card
                    carte_da_buttare_nel_mazzo -= 1
                else:
                    giocatore_corrente *= -1  # no court cards found yet, back to other giocatore_corrente
            else:
                # court card found, back to the other giocatore_corrente
                partita_in_corso = True
                carte_da_buttare_nel_mazzo = prossima_carta
                giocatore_corrente *= -1
        #end while

        #presa successiva
        #TODO: ATTENZIONE, in straccia camicia la regola e' opposta: prende il mazzo chi ha vinto
        # end of trick, make the losing giocatore_corrente pick up the cards in the mazzo_in_tavola
        prese +=  1
        # giocatore_corrente contiene il flag del prossimo giocatore_corrente che deve giocare
        if giocatore_corrente == 1:
            #deve giocare il primo giocatore -> l
            mazzo_giocatore_due.extend(mazzo_in_tavola)
            mazzo_in_tavola = []
        else:
            mazzo_giocatore_uno.extend(mazzo_in_tavola)
            mazzo_in_tavola = []

        giocatore_corrente *= -1

        if(mazzo_giocatore_uno == mazzo_iniziale_giocatore_uno and mazzo_giocatore_due==mazzo_iniziale_giocatore_due ):
            print(process, "-", "siamo tornati da capo:", mazzo_giocatore_uno,mazzo_giocatore_due)
            print ("%s - Ci sono stati %d turni e %d prese" % (process, turni, prese))
            #commentato per vedere loop`
            return 0

        # print current status
        if verbose:
            print (process, "-", "Situazione:", mazzo_giocatore_uno, mazzo_giocatore_due)

    if not fast:
        print ("%s - Ci sono stati %d turni e %d prese" % (process, turni, prese))
