# Sign in with Apple

A library facilitating the server-side validation of Sign in with Apple (SIWA)
identity tokens.

This library has a very narrow focus. It addresses a small subset of the
potential ways in which SIWA can be used. It does not attempt to address the
web-based SIWA flow. It abstracts away RSA256, JSON Web Tokens, and other
machinery used by SIWA, and attempts to provide a simple, clean interface for
application development.

## The problem this library solves

Suppose you have a macOS or iOS application. You present the SIWA interface
(the "Sign in with Apple" button) to a user using 
[`AuthenticationServices`](https://developer.apple.com/documentation/authenticationservices).
They sign in. Your app is provided with an instance of
[`ASAuthorizationAppleIDCredential`](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential)
(the "client side credential"), containing data describing the user.

Suppose your system is controlled by a platform agnostic application
programming interface (API). You wish to create a new user account, or
sign in an existing user, via your API. Your app makes an HTTP request to your
API asking it to create a new user or sign in an existing user based on the
data contained the client side credential.

How do you know the data was provided by `AuthenticationServices`, and not
just smashed together in a text editor? That is, how do you know the
data are _authentic_ on the server side?

Apple facilitates the authentication of the credential by providing a blob
of data in the `ASAuthorizationAppleIDCredential.identityToken` property. This
identity token contains a JSON Web Token ("JWT"), a standardised format for
carrying credentials.


Validation of the credential may be achieved via asymmetric cryptography, using
the RSA256 algorithm. Apple retains a secret encryption key, and publishes a
related public key. Apple creates signature (a large string of text) using two
inputs: Their private key, and the contents of the client side credential.

External parties like your API can verify the authenticity of that signature,
and therefore the associated credential, using the public key published by
Apple.

This library performs the following functions with respect to the above
process:

1. Retrieves Apple's public key
2. Parses an identity token (`ASAuthorizationAppleIDCredential.identityToken`)
3. Provides a boolean flag asserting that the credential is valid or not valid
4. Provides convenient access to the content of the identity token (e.g 
the user email address)

## Installation

Install Sign in with Apple via PyPi:

```
pip install siwa
```

## Dependencies

This library is heavily dependent on
[`PyJWT`](https://github.com/jpadilla/pyjwt). All validation of identity
tokens is peformed by `PyJWT`.

Marshalling of the Apple public RSA key into PKS12 format is performed by
the [`PythonRSA`](https://github.com/sybrenstuvel/python-rsa/) library.

## Usage

```python
from siwa import IdentityToken, KeyCache

cache = KeyCache()  # The cache is optional but will reduce the time taken
                    # to validate tokens using the same public key

token = IdentityToken.parse(data=json_string)

token_is_valid = token.is_validly_signed(key_cache=cache)

# if `token_is_valid` is True, you can confidently proceed with the credential

# Useful properties:
print(token.payload.email)
print(token.payload.unique_apple_user_id)
print(token.issued_utc_seconds_since_epoch)
```


## Testing

To test the library, create a file that contains a valid SIWA identity token.
For example, one that you have obtained from `AuthenticationServices` in
Xcode.

Run `test.py`, passing the relative path to that file under the
`--example-jwt-file` parameter:

```
python3 test.py --example-jwt-file example/jwt/file
```

## Contact

[@hugh_jeremy](https://twitter.com/hugh_jeremy) on Twitter or email
[hugh@blinkybeach.com](mailto:hugh@blinkybeach.com)
