# Stat 650 Miniproject

*Completed as a final project for Carnegie Mellon University's 36650 Graduate Statistical Computing course*

Let $c_1$, $c_2$, . . . , $c_n$ be a sequence of $n$ encrypted characters, and let $b(c, c′)$ be the frequency of character
pair($c$, $c′$) in a reference text.

We assume that we can decrypt our text using a substitution decryption d which maps a given character
to another character bijectively. Then, $d(c_1)$, . . . , $d(c_n)$ is our decoded text under $d$. We do not know the
mapping $d$ so our task is to statistically estimate the most likely $d$.

We assign each decryption $d$ a score

$L(d) = \prod_{i=2}^{n} b(d(c_{i−1}), d(c_i))$.

Large $L$ is preferred, so we want to find the d that maximizes $L(d)$, at least approximately.

The Markov chain we construct will sample the space of decryptions $d$. In other words, we will construct
a stochastic process that moves from one decryption to another according to certain rules. The chain is
constructed so that it asymptotically samples d from the distribution $\pi(d) = \frac{L(d)^p}{\sum_{d'}L(d′)^p},
where p > 0 is a parameter. The algorithm (called the *Metropolis algorithm*) that produces a Markov chain with the
required properties is as follows:

1. Choose an initial decryption key d (e.g., the identity mapping).

2. Repeat the following steps for many iterations (e.g., 10 000):

- Given the current decryption *d*, randomly sample a candidate decryption from a pre-specified
proposal distribution *q(d′|d)*.

- Sample an independent Uniform(0, 1) random variable *U*.

- If *U* < $\frac{\pi(d')}{\pi(d)} = (\frac{L(d)}{\sum_{d'}L(d′)})^p$, move to decryption d′, else remain in decryption d.

As we let the algorithm run, we store the decryption key with the largest value of *L*. This will produce
our best-fitting decryption.
